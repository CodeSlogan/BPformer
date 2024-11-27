import torch
import torch.nn as nn
import torch.optim as optim
from data_process.DataModule import DataModule2
from datetime import datetime
from model.timemixer.TimeMixer import TimeMixer
import argparse
from utils.eval_func import *

device = torch.device("cuda:2" if torch.cuda.is_available() else "cpu")

parser = argparse.ArgumentParser(description='TimeMixer')

# data loader
parser.add_argument('--features', type=str, default='M',
                    help='forecasting task, options:[M, S, MS]; M:multivariate predict multivariate, S:univariate predict univariate, MS:multivariate predict univariate')
parser.add_argument('--target', type=str, default='OT', help='target feature in S or MS task')
parser.add_argument('--freq', type=str, default='h',
                    help='freq for time features encoding, options:[s:secondly, t:minutely, h:hourly, d:daily, b:business days, w:weekly, m:monthly], you can also use more detailed freq like 15min or 3h')
parser.add_argument('--checkpoints', type=str, default='./checkpoints/', help='location of model checkpoints')

# forecasting task
parser.add_argument('--seq_len', type=int, default=1024, help='input sequence length')
parser.add_argument('--label_len', type=int, default=0, help='start token length')
parser.add_argument('--pred_len', type=int, default=1024, help='prediction sequence length')
parser.add_argument('--seasonal_patterns', type=str, default='Monthly', help='subset for M4')
parser.add_argument('--inverse', action='store_true', help='inverse output data', default=False)

# model define
parser.add_argument('--top_k', type=int, default=5, help='for TimesBlock')
parser.add_argument('--num_kernels', type=int, default=6, help='for Inception')
parser.add_argument('--enc_in', type=int, default=2, help='encoder input size')
parser.add_argument('--dec_in', type=int, default=2, help='decoder input size')
parser.add_argument('--c_out', type=int, default=2, help='output size')
parser.add_argument('--d_model', type=int, default=16, help='dimension of model')
parser.add_argument('--n_heads', type=int, default=4, help='num of heads')
parser.add_argument('--e_layers', type=int, default=3, help='num of encoder layers')
parser.add_argument('--d_layers', type=int, default=1, help='num of decoder layers')
parser.add_argument('--d_ff', type=int, default=32, help='dimension of fcn')
parser.add_argument('--moving_avg', type=int, default=25, help='window size of moving average')
parser.add_argument('--factor', type=int, default=1, help='attn factor')
parser.add_argument('--distil', action='store_false',
                    help='whether to use distilling in encoder, using this argument means not using distilling',
                    default=True)
parser.add_argument('--dropout', type=float, default=0.1, help='dropout')
parser.add_argument('--embed', type=str, default='timeF',
                    help='time features encoding, options:[timeF, fixed, learned]')
parser.add_argument('--activation', type=str, default='gelu', help='activation')
parser.add_argument('--output_attention', action='store_true', help='whether to output attention in ecoder')
parser.add_argument('--channel_independence', type=int, default=0,
                    help='0: channel dependence 1: channel independence for FreTS model')
parser.add_argument('--decomp_method', type=str, default='moving_avg',
                    help='method of series decompsition, only support moving_avg or dft_decomp')
parser.add_argument('--use_norm', type=int, default=1, help='whether to use normalize; True 1 False 0')
parser.add_argument('--down_sampling_layers', type=int, default=3, help='num of down sampling layers')
parser.add_argument('--down_sampling_window', type=int, default=2, help='down sampling window size')
parser.add_argument('--down_sampling_method', type=str, default='avg',
                    help='down sampling method, only support avg, max, conv')
parser.add_argument('--use_future_temporal_feature', type=int, default=0,
                    help='whether to use future_temporal_feature; True 1 False 0')

# imputation task
parser.add_argument('--mask_rate', type=float, default=0.25, help='mask ratio')

# anomaly detection task
parser.add_argument('--anomaly_ratio', type=float, default=0.25, help='prior anomaly ratio (%)')

# optimization
parser.add_argument('--num_workers', type=int, default=10, help='data loader num workers')
parser.add_argument('--itr', type=int, default=1, help='experiments times')
parser.add_argument('--train_epochs', type=int, default=800, help='train epochs')
parser.add_argument('--batch_size', type=int, default=1024, help='batch size of train input data')
parser.add_argument('--patience', type=int, default=10, help='early stopping patience')
parser.add_argument('--learning_rate', type=float, default=0.0007, help='optimizer learning rate')
parser.add_argument('--des', type=str, default='test', help='exp description')
parser.add_argument('--loss', type=str, default='MSE', help='loss function')
parser.add_argument('--lradj', type=str, default='TST', help='adjust learning rate')
parser.add_argument('--pct_start', type=float, default=0.2, help='pct_start')
parser.add_argument('--use_amp', action='store_true', help='use automatic mixed precision training', default=False)
parser.add_argument('--comment', type=str, default='none', help='com')

# GPU
parser.add_argument('--use_gpu', type=bool, default=True, help='use gpu')
parser.add_argument('--gpu', type=int, default=0, help='gpu')
parser.add_argument('--use_multi_gpu', action='store_true', help='use multiple gpus', default=False)
parser.add_argument('--devices', type=str, default='0,1', help='device ids of multile gpus')

# de-stationary projector params
parser.add_argument('--p_hidden_dims', type=int, nargs='+', default=[128, 128],
                    help='hidden layer dimensions of projector (List)')
parser.add_argument('--p_hidden_layers', type=int, default=2, help='number of hidden layers in projector')

args = parser.parse_args()
print('args:', args)

input1_scaler, input2_scaler, output_scaler, train_dataloader, test_dataloader = DataModule2(args)
print("Load data done!")

# Initialize model
model = TimeMixer(args).to(device)
# 超参数
num_epochs = args.train_epochs
learning_rate = args.learning_rate

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

is_train = False
if is_train:
    # 训练模型
    for epoch in range(num_epochs):
        print(f"{epoch}/{num_epochs}")
        step = 0
        model.train()
        for batch_inputs, batch_targets in train_dataloader:
            step += 1
            if step % 10 == 0:
                print(f"epoch:{epoch}, {step}/{len(train_dataloader)}")

            batch_inputs = batch_inputs.to(device)
            batch_targets = batch_targets.to(device)
            batch_inputs = batch_inputs.permute(0, 2, 1)

            outputs = model(batch_inputs)

            loss = criterion(outputs, batch_targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

        if epoch and epoch % 50 == 0:
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"model/param/timemixer_{current_time}_epoch{epoch}.pth"
            torch.save(model.state_dict(), file_name)
            print(f"timemixer_{current_time}_epoch{epoch} save succesfully")

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"model/param/timemixer_{current_time}_epoch{num_epochs}.pth"
    torch.save(model.state_dict(), file_name)
    print("The model has been saved successfully!")
else:
    model.load_state_dict(torch.load('model/param/timemixer_20241111_221639_epoch150.pth'))

    model.eval()  # 设置模型为评估模式
    total_loss = 0
    inverse_loss = 0
    MAE_SBP, MSE_SBP, MAE_DBP, MSE_DBP = [], [], [], []
    SD_SBP, SD_DBP = [], []
    SBP5, SBP10, SBP15 = [], [], []
    DBP5, DBP10, DBP15 = [], [], []

    with (torch.no_grad()):  # 在评估过程中不需要计算梯度
        for batch_inputs, batch_targets in test_dataloader:
            batch_inputs = batch_inputs.to(device)
            batch_targets = batch_targets.to(device)
            batch_inputs = batch_inputs.permute(0, 2, 1)

            # 前向传播
            outputs = model(batch_inputs)

            # 计算损失
            loss = criterion(outputs, batch_targets)
            total_loss += loss.item()

            outputs_inver = output_scaler.inverse_transform(outputs.cpu())
            batch_targets_inver = output_scaler.inverse_transform(batch_targets.cpu())
            inverse_loss += mse_loss(outputs_inver, batch_targets_inver)

            mae_sbp, mse_sbp, mae_dbp, mse_dbp, sd_peaks, sd_troughs, peak_percentages, trough_percentages = calculate_batch_errors(
                outputs_inver, batch_targets_inver)
            MAE_SBP.append(mae_sbp)
            MSE_SBP.append(mse_sbp)
            MAE_DBP.append(mae_dbp)
            MSE_DBP.append(mse_dbp)
            SD_SBP.append(sd_peaks)
            SD_DBP.append(sd_troughs)
            SBP5.append(peak_percentages[0])
            SBP10.append(peak_percentages[1])
            SBP15.append(peak_percentages[2])
            DBP5.append(trough_percentages[0])
            DBP10.append(trough_percentages[1])
            DBP15.append(trough_percentages[2])

    average_loss = total_loss / len(test_dataloader)
    rmse_loss = torch.sqrt(torch.tensor(average_loss))
    inverse_loss = inverse_loss / len(test_dataloader)
    print(f"average_loss: {average_loss:.4f}")
    print(f"RMSE Loss: {rmse_loss.item():.4f}")
    print(f"归一化前总loss: {inverse_loss.item():.4f}")
    print(f"MAE SBP: {np.mean(MAE_SBP):.4f}")
    print(f"MSE SBP: {np.mean(MSE_SBP):.4f}")
    print(f"SD_SBP: {np.mean(SD_SBP):.4f}")
    print(f"MAE DBP: {np.mean(MAE_DBP):.4f}")
    print(f"MSE DBP: {np.mean(MSE_DBP):.4f}")
    print(f"SD_DBP: {np.mean(SD_DBP):.4f}")

    print(f"SBP5: {np.mean(SBP5) * 100:.4f}%, SBP10: {np.mean(SBP10) * 100:.4f}%, SBP15: {np.mean(SBP15) * 100:.4f}%")
    print(f"DBP5: {np.mean(DBP5) * 100:.4f}%, DBP10: {np.mean(DBP10) * 100:.4f}%, DBP15: {np.mean(DBP15) * 100:.4f}%")