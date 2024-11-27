**![BHS.png](image/BHS.png)

![AAMI.png](image/AAMI.png)

# 数据集2mat

|         模型名称         | average_mse_loss | RMSE Loss | 归一化前总loss | MAE SBP | MSE SBP | SD_SBP | MAE DBP | MSE DBP | SD_DBP | 
|:--------------------:|:----------------:|:---------:|:---------:|:-------:|:-------:|:------:|:-------:|:-------:|:------:|
|    medformer-250     |      0.0026      |  0.0509   |  56.5940  | 6.1633  | 90.4140 | 7.3660 | 4.1184  | 45.6402 | 5.8848 |
| :star2:medformer-450 |      0.0019      |  0.0439   |  41.6732  | 4.5599  | 65.6873 | 6.6094 | 3.3395  | 37.1549 | 5.3365 |
|    medformer-500     |      0.0024      |  0.0487   |  50.9964  | 5.3919  | 83.1704 | 7.3433 | 3.8347  | 43.9991 | 5.9614 |
|    medformer-750     |      0.0028      |  0.0529   |  59.5841  | 5.6961  | 89.9946 | 7.6294 | 4.5455  | 56.6079 | 6.4364 |
|    medformer-1024    |      0.0032      |  0.0563   |  66.7901  | 6.1280  | 95.3150 | 7.5393 | 5.0020  | 64.8453 | 6.4997 |
|                      |                  |           |           |         |         |        |         |         |        |

|         模型名称         | MAE SBP | SD_SBP | MAE DBP | SD_DBP |   SBP5   |  SBP10   |  SBP15   |   DBP5   |  DBP10   |  DBP15   |
|:--------------------:|:-------:|:------:|:-------:|:------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|    medformer-250     | 6.1633  | 7.3660 | 4.1184  | 5.8848 | 57.9576% | 83.3168% | 92.9048% | 73.0711% | 91.2009% | 95.8557% |
| :star2:medformer-450 | 4.5599  | 6.6094 | 3.3395  | 5.3365 | 72.3428% | 90.6339% | 95.2322% | 80.9273% | 93.5162% | 96.6554% |
|    medformer-500     | 5.3919  | 7.3433 | 3.8347  | 5.9614 | 65.2123% | 87.5938% | 94.1185% | 75.9935% | 91.6040% | 95.8419% |
|    medformer-750     | 5.6961  | 7.6294 | 4.5455  | 6.4364 | 63.6744% | 85.3470% | 92.5608% | 70.4665% | 88.8688% | 94.4794% |
|    medformer-1024    | 6.1280  | 7.5393 | 5.0020  | 6.4997 | 60.1533% | 83.4659% | 91.5994% | 66.7803% | 87.4745% | 93.8422% |
|                      |         |        |         |        |          |          |          |          |          |          |

> pred_len = 500

- bpformerv2: medformer + moderntcn (embedding)

|      模型名称      | average_mse_loss | RMSE Loss | 归一化前总loss | MAE SBP | MSE SBP | SD_SBP | MAE DBP | MSE DBP | SD_DBP | 
|:--------------:|:----------------:|:---------:|:---------:|:-------:|:-------:|:------:|:-------:|:-------:|:------:|
|   medformer    |      0.0024      |  0.0487   |  50.9964  | 5.3919  | 83.1704 | 7.3433 | 3.8347  | 43.9991 | 5.9614 |
|   med_covn1d   |      0.0024      |  0.0487   |  51.1158  | 5.5773  | 79.6933 | 7.0824 | 3.8730  | 44.2924 | 5.9442 |
|   bpformerv2   |      0.0021      |  0.0460   |  45.5169  | 4.5988  | 69.5007 | 7.1880 | 3.2951  | 36.7769 | 5.6905 |
| bpformerv2-450 |      0.0022      |  0.0472   |  48.0905  | 4.5988  | 70.7077 | 7.2671 | 3.3219  | 38.5745 | 5.8501 |
|                |                  |           |           |         |         |        |         |         |        |

|      模型名称      | MAE SBP | SD_SBP | MAE DBP | SD_DBP |   SBP5   |  SBP10   |  SBP15   |   DBP5   |  DBP10   |  DBP15   |
|:--------------:|:-------:|:------:|:-------:|:------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|   medformer    | 5.3919  | 7.3433 | 3.8347  | 5.9614 | 65.2123% | 87.5938% | 94.1185% | 75.9935% | 91.6040% | 95.8419% |
|   med_covn1d   | 5.5773  | 7.0824 | 3.8730  | 5.9442 | 61.9891% | 86.4202% | 94.1229% | 75.4264% | 91.4894% | 95.9496% |
|   bpformerv2   | 4.5988  | 7.1880 | 3.2951  | 5.6905 | 72.7132% | 89.7024% | 94.6711% | 80.9264% | 93.2245% | 96.5440% |
| bpformerv2-450 | 4.5988  | 7.2671 | 3.3219  | 5.8501 | 73.0087% | 89.5662% | 94.4124% | 81.1942% | 92.9275% | 96.1866% |
|                |         |        |         |        |          |          |

> pred_len = 1024

|             模型名称             | average_mse_loss | RMSE Loss  |  归一化前总loss  |  MAE SBP   |   MSE SBP   |   SD_SBP   |  MAE DBP   |   MSE DBP   |   SD_DBP   | 
|:----------------------------:|:----------------:|:----------:|:-----------:|:----------:|:-----------:|:----------:|:----------:|:-----------:|:----------:|
|         cnn-lstm-ppg         |      0.0134      |   0.1155   |  281.4627   |  14.2112   |  437.2165   |  15.4965   |  11.9072   |  303.5553   |  12.4827   | 
|    :star:**patchtst-ppg**    |      0.0042      |   0.0645   |   87.8265   |   7.6219   |  138.1481   |   8.8635   |   5.1728   |   77.4795   |   7.3165   |
|       patchtst-ppg+ecg       |      0.0048      |   0.0690   |  100.4596   |   8.7074   |  159.9748   |   9.1281   |   5.7956   |   81.5585   |   7.2161   | 
|  :star:crossformer-ppg+ecg   |      0.0038      |   0.0619   |   80.7775   |   7.0393   |  123.0274   |   8.6584   |   5.0378   |   67.1356   |   6.9595   | 
|        softs-ppg+ecg         |      0.0087      |   0.0935   |  184.4033   |  11.4373   |  287.6602   |  12.4303   |   8.0717   |  153.8381   |   9.6523   |
| :star2:**medformer-ppg+ecg** |    **0.0032**    | **0.0563** | **66.7901** | **6.1280** | **95.3150** | **7.5393** | **5.0020** | **64.8453** | **6.4997** |
|     *medformer-ppg+ppg*      |      0.0046      |   0.0679   |   97.3559   |   7.1812   |  134.3557   |   9.0748   |   5.9154   |   94.7465   |   7.9205   | 
|      *medf_dec-ppg+ecg*      |      0.0044      |   0.0660   |   91.8299   |   7.3256   |  137.3974   |   9.0064   |   5.7106   |   84.6292   |   7.4437   | 
|     itransformer-ppg+ecg     |      0.0381      |   0.1953   |  803.8553   |  34.7486   |  1820.0414  |  23.6844   |  23.1626   |  724.5032   |  13.9485   |
|      timemixer-ppg+ecg       |      0.0086      |   0.0929   |  181.9439   |  12.1272   |  281.1597   |  11.8479   |   9.0559   |  160.2216   |   9.3849   | 
|     *bpformerv1-ppg+ecg*     |      0.0041      |   0.0642   |   87.0462   |   7.3303   |  126.6045   |   8.6217   |   5.9230   |   82.6581   |   7.2454   | 
|        msgnet-ppg+ecg        |      0.0079      |   0.0888   |  166.3099   |  11.2094   |  255.4992   |  11.3036   |   8.2832   |  144.4841   |   8.8842   |
|   :star:moderntcn-ppg+ecg    |      0.0036      |   0.0603   |   76.7211   |   7.3628   |  110.6512   |   7.7655   |   6.2649   |   69.8185   |   6.1324   |
|   :star:  tslanet-ppg+ecg    |      0.0048      |   0.0694   |  101.4517   |   8.8342   |  171.7770   |   9.8799   |   6.5382   |   93.3845   |   7.6086   |
|      samformer-ppg+ecg       |      0.0192      |   0.1386   |  404.9842   |  17.7816   |  548.6365   |  15.4997   |  14.6515   |  379.9878   |  13.2210   |
|        vqmtm-ppg+ecg         |      0.0079      |   0.0891   |  167.4536   |  11.8605   |  275.8050   |  11.7537   |  11.7537   |  219.9587   |   9.9601   |
|       attraos-ppg+ecg        |      0.0108      |   0.1040   |  228.2148   |  13.6945   |  342.5528   |  12.5513   |  10.7313   |  214.2452   |  10.1329   |
|                              |                  |            |             |            |             |            |            |             |            |

|             模型名称             |     SBP5     |    SBP10     |    SBP15     |     DBP5     |    DBP10     |    DBP15     |
|:----------------------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|         cnn-lstm-ppg         |   31.3120%   |   53.1457%   |   66.9534%   |   35.7605%   |   58.5621%   |   71.9409%   |
|     :star: patchtst-ppg      |   50.8755%   |   76.6832%   |   87.5988%   |   66.0458%   |   87.4029%   |   93.6918%   |
|       patchtst-ppg+ecg       |   43.1019%   |   71.0369%   |   84.8365%   |   58.3990%   |   84.3652%   |   92.5187%   |
|  :star: crossformer-ppg+ecg  |   53.5731%   |   78.0768%   |   87.9761%   |   65.9951%   |   85.8339%   |   92.0496%   |
|        softs-ppg+ecg         |   39.3100%   |   62.0124%   |   74.9886%   |   48.3626%   |   73.0579%   |   84.8845%   |
| :star2:**medformer-ppg+ecg** | **60.1533%** | **83.4659%** | **91.5994%** | **66.7803%** | **87.4745%** | **93.8422%** |
|     *medformer-ppg+ppg*      |   55.1557%   |   79.2201%   |   88.6656%   |   60.9970%   |   83.7954%   |   91.8172%   |
|      *medf_dec-ppg+ecg*      |   54.7382%   |   78.7711%   |   88.4774%   |   61.8139%   |   84.6041%   |   92.2181%   |
|     itransformer-ppg+ecg     |   8.3409%    |   17.8118%   |   27.3166%   |   8.9763%    |   18.7078%   |   29.4122%   |
|      timemixer-ppg+ecg       |   32.2385%   |   55.6205%   |   70.8680%   |   39.5132%   |   66.0864%   |   81.2493%   |
|     *bpformerv1-ppg+ecg*     |   54.0965%   |   79.1464%   |   88.9411%   |   60.9133%   |   84.5202%   |   92.4475%   |
|        msgnet-ppg+ecg        |   36.7638%   |   60.4308%   |   74.5848%   |   44.7250%   |   70.7934%   |   83.9277%   |
|   :star: moderntcn-ppg+ecg   |   42.1023%   |   77.6080%   |   90.6637%   |   45.2037%   |   84.2305%   |   94.8561%   |
|   :star:  tslanet-ppg+ecg    |   45.0208%   |   70.3839%   |   82.7702%   |   53.3640%   |   80.1113%   |   90.3460%   |
|      samformer-ppg+ecg       |   20.5109%   |   38.4126%   |   53.1031%   |   23.6372%   |   44.5468%   |   60.9951%   |
|        vqmtm-ppg+ecg         |   33.1981%   |   57.3756%   |   72.0750%   |   31.0858%   |   56.8358%   |   73.9686%   |
|       attraos-ppg+ecg        |   26.2731%   |   48.7697%   |   65.8062%   |   31.0292%   |   56.5868%   |   74.7473%   |
|                              |              |              |              |              |              |              |

# 数据集1csv

|    模型    | average_loss | RMSE Loss |   归一化前   |
|:--------:|:------------:|:---------:|:--------:|
| patchtst |    0.0042    |  0.0651   | 88.2288  |
| cnn-lstm |    0.0082    |  0.0906   | 170.6542 |**
