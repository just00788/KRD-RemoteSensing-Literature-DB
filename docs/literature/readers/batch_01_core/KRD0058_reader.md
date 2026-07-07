# Full-Paper Reader: 基于多源数据的石漠化地区裸岩信息提取和景观格局分析

## 1. Bibliographic Information

- Paper ID: KRD0058
- Title: 基于多源数据的石漠化地区裸岩信息提取和景观格局分析
- Translated title if applicable: unknown
- Authors: unknown
- Year: 2024
- Journal / Source: 万方学位论文
- DOI: unknown
- URL: https://d.wanfangdata.com.cn/thesis/ChhUaGVzaXNOZXdTMjAyNDA5MjAxNTE3MjUSCUQwMjYxNjM3ORoIbHNrZncxbmQ%3D
- PDF path: `docs/literature/pdfs/package_2000_2026/基于多源数据的石漠化地区裸岩信息提取和景观格局分析_张志慧.pdf`
- Language: Chinese
- Readability status: ready
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.4, p.7, p.10
- Introduction: p.10, p.13
- Study Area: p.10, p.14, p.15, p.16, p.19, p.22, p.23, p.26, p.29, p.30, p.31, p.32, ...
- Data: p.1, p.2, p.4, p.7, p.10, p.11, p.13, p.15, p.16, p.17, p.18, p.19, ...
- Methods: p.4, p.5, p.7, p.8, p.11, p.15, p.16, p.17, p.18, p.21, p.27, p.33, ...
- Experiments: p.14, p.32, p.33, p.38, p.40, p.41, p.45, p.50, p.58, p.72
- Results: p.4, p.5, p.7, p.8, p.11, p.13, p.15, p.16, p.17, p.18, p.19, p.24, ...
- Discussion: not located
- Conclusions: p.17, p.68
- References: p.12, p.70
- Figures/Tables captions: 25 located
  - p.20: 图 1-1 技术路线图
  - p.22: 图 2-1 研究区地理位置图
  - p.25: 表 2-1 哨兵 2 号遥感影像波段
  - p.26: 表 2-2 Landsat 8 OLI 遥感影像波段信息
  - p.26: 表 2-3 数据来源信息
  - p.27: 图 2-2 Landsat 8 辐射定标与大气校正前后植被光谱曲线对比
  - p.30: 图 2-3 无人机影像飞行图
  - p.31: 图 2-5 是处理好的无人机影像。

## 3. Abstract-Level Understanding

Source anchors: p.1

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `bare_rock_fraction_fbr` 相关，关键词信号包括 `unknown`。
- 研究目标: 基于多源数据的石漠化地区裸岩信息提取和景观格局分析
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> 硕 士 学 位 论 文 基于多源数据的石漠化地区裸岩信息提取 和景观格局分析 学科专业 地图学与地理信息系统 学位类型 □√科学学位 □专业学位 研究生姓名 张志慧 导师姓名、职称 刘雯 副教授 论文编号 201820131099 湖南师范大学学位评定委员会办公室 二 O 二一年五月 分类号 密级 公开 学校代码 10542 学号 201820131099 基于多源数据的石漠化地区裸岩信息提取 和景观格局分析 Study on Information extraction and Spatial Distribution Pattern of Rock in Rocky Desertification Area Based on multi-source data 研 究 生 姓 名 张志慧 导师姓名职称 刘雯 副教授 学 科 专 业 地图学与地理信息系统 研 究 方 向 生态环境遥感 湖南师范大学学位评定委员会办公室 二〇二一年五月

## 4. Introduction Reading Notes

- Source anchors: p.10, p.13
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.4: 喀斯特地区不同石漠化等级的结构和格局是实现区域石漠化治
- p.4: 在石漠化地区， 根据岩石的出露程度不同可划分不同石漠化
- p.4: 程度，基岩裸露率是判别石漠化强度的重要指标，基岩裸露率越高，
- p.4: 以往研究以大尺度遥感影像提取石漠化信息为主， 本研究采用大
- p.4: 尺度遥感影像和小尺度无人机航摄影像共同提取石漠化地区的裸岩
- p.4: 对石漠化地区裸岩信息采用不同的方法提取， 获取不同影像分辨率条
- p.4: 件下裸岩分布进而得到普定县裸岩率分布图， 使用无人机航摄影像对
- p.4: 据预处理后使用两种裸岩率信息提取方法，再对比 11 幅无人机数据
- p.4: 提取裸岩信息的结果。结果表明，基于归一化岩石指数计算的基岩裸
- p.4: 露率值为 70%和 82%， 像元二分法计算的基岩裸露率值为68%和 76%，
- p.9: The small-scale patch landscape
- p.9: Therefore, small scale stu dy has important
- p.52: NDVI NDVIsoilVC NDVIveg NDVIsoil
- p.54: 计算方法和上述归一化岩石指数一样， 先计算出影像的NDVI 值和𝑆𝑖值， 根据前


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.10, p.14, p.15, p.16, p.19, p.22, p.23, p.26, p.29, p.30, p.31, p.32, ...
- Geographic/environmental background: extract from Study Area anchors; manual confirmation needed for exact place names and environmental facts.
- Satellite data: see evidence below.
- DEM/topographic data: see evidence below.
- Field data: see evidence below if `field/sample/reference` appears.
- UAV data: see evidence below if `UAV` appears.
- Reference data: see validation evidence in Section 8.
- Temporal coverage: record only when explicitly visible in evidence excerpts.
- Spatial resolution: record only when explicitly visible in evidence excerpts.
- Preprocessing steps: see Method Workflow.

Data evidence:
- p.4: 本研究使用遥感影像数据（Landsat-8 和 Sentinel-2A 卫星数据）
- p.4: 法计算的裸岩率。Sentinel-2A 数据对裸岩率提取使用直接计算归一化
- p.7: The results show that sentinel -2A
- p.8: selected to classify the UAV image of rocky desertification.
- p.8: the UAV image is interpreted, and then the distribution characteristics of
- p.9: Key words: Object-oriented classification; UAV; Classification; bare
- p.15: 标。2002 年，童立强[8]使用对数剩余变换对 Landsat 影像数据进行预处理，对校
- p.15: 数。2009 年 Huang 等[9]根据归一化植被指数的计算方法使用 Landsat 数据中的中
- p.17: [32]人使用高分辨率卫星数据 QUICKBIRD 卫星影像，应用多尺度分割技术对影
- p.18: 研究选取 Landsat-8 分辨率为 30m 的遥感数据和 Sentinel-2A 分辨率为 10m


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.4: 喀斯特地区不同石漠化等级的结构和格局是实现区域石漠化治
- p.4: 在石漠化地区， 根据岩石的出露程度不同可划分不同石漠化
- p.4: 程度，基岩裸露率是判别石漠化强度的重要指标，基岩裸露率越高，
- p.4: 以往研究以大尺度遥感影像提取石漠化信息为主， 本研究采用大
- p.4: 尺度遥感影像和小尺度无人机航摄影像共同提取石漠化地区的裸岩
- p.4: 对石漠化地区裸岩信息采用不同的方法提取， 获取不同影像分辨率条
- p.4: 件下裸岩分布进而得到普定县裸岩率分布图， 使用无人机航摄影像对
- p.4: 据预处理后使用两种裸岩率信息提取方法，再对比 11 幅无人机数据
- p.4: 提取裸岩信息的结果。结果表明，基于归一化岩石指数计算的基岩裸
- p.4: 露率值为 70%和 82%， 像元二分法计算的基岩裸露率值为68%和 76%，


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: located
- DEM/topographic variables: located
- LSMM/SMA/MESMA/FCLS: located
- machine learning models: located
- deep learning models: not reported
- semantic segmentation architecture: not reported
- training strategy: located
- sample split: located
- cross-validation: not reported
- cross-region validation: not reported
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.9: The small-scale patch landscape
- p.9: Therefore, small scale stu dy has important
- p.52: NDVI NDVIsoilVC NDVIveg NDVIsoil
- p.54: 计算方法和上述归一化岩石指数一样， 先计算出影像的NDVI 值和𝑆𝑖值， 根据前
- p.54: 期处理的前期的预处理得到 NDVI 图像， 然后计算NDVI 中的最值， 根据影像中
- p.54: 的 2 个极值对应的 NDVI 值作为𝑁𝐷𝑉𝐼𝑚𝑎𝑥和𝑁𝐷𝑉𝐼𝑚𝑖𝑛作为影像中置信区间的最大
- p.54: 假设置信度为1， 采用累计频率中1%的 NDVI 值为𝑁𝐷𝑉𝐼0， 累计频
- p.54: 率 99%的 NDVI 值是𝑁𝐷𝑉𝐼𝑟。根据式 4-4 中，计算当 NDVI<𝑁𝐷𝑉𝐼𝑟，𝑉𝐶取值为
- p.54: 0；而当 NDVI>𝑁𝐷𝑉𝐼𝑟，𝑉𝐶取值为 1。同理，计算出土壤裸露率。然后根据公式
- p.70: The composite vegetation indexes and spatial analysis applied to rockdesertification information extraction[J].
- p.71: small-scale landscape elements - ScienceDirect[J].
- p.72: retrieval of surface reflectances from TM images[J].
- p.4: 本研究使用遥感影像数据（Landsat-8 和 Sentinel-2A 卫星数据）
- p.4: 法计算的裸岩率。Sentinel-2A 数据对裸岩率提取使用直接计算归一化
- p.7: The results show that sentinel -2A
- p.8: selected to classify the UAV image of rocky desertification.
- p.8: the UAV image is interpreted, and then the distribution characteristics of
- p.9: Key words: Object-oriented classification; UAV; Classification; bare
- p.15: 标。2002 年，童立强[8]使用对数剩余变换对 Landsat 影像数据进行预处理，对校
- p.15: 数。2009 年 Huang 等[9]根据归一化植被指数的计算方法使用 Landsat 数据中的中
- p.17: [32]人使用高分辨率卫星数据 QUICKBIRD 卫星影像，应用多尺度分割技术对影
- p.18: 研究选取 Landsat-8 分辨率为 30m 的遥感数据和 Sentinel-2A 分辨率为 10m


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: not located
- Classification metrics located: OA, Kappa, Precision, IoU

Metric evidence:
- p.2: Study on Information extraction and Spatial
- p.2: Distribution Pattern of Rock in Rocky
- p.7: The change of landscape pattern has an important influence on the
- p.7: pattern in rocky desertification area fo r the development of rocky
- p.7: used to compare two different remote sensing image data to verify the
- p.7: accuracy of the calculation results.
- p.7: Spatial distribution of rock under bare rock
- p.8: based on pixels cannot meet the requirements of extraction accuracy of
- p.8: selected to classify the UAV image of rocky desertification.
- p.8: shows that the object -oriented classification h as higher accuracy, it can
- p.8: the UAV image is interpreted, and then the distribution characteristics of
- p.8: rock patches unde r different bare rock rates are obtained by combining the


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.20
- Caption: 图 1-1 技术路线图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 2
- Source anchor: p.22
- Caption: 图 2-1 研究区地理位置图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 3
- Source anchor: p.25
- Caption: 表 2-1 哨兵 2 号遥感影像波段
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.26
- Caption: 表 2-2 Landsat 8 OLI 遥感影像波段信息
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.26
- Caption: 表 2-3 数据来源信息
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.27
- Caption: 图 2-2 Landsat 8 辐射定标与大气校正前后植被光谱曲线对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.30
- Caption: 图 2-3 无人机影像飞行图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.31
- Caption: 图 2-5 是处理好的无人机影像。
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.31
- Caption: 图 2-4 未处理前无人机航摄影像图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.31
- Caption: 图 2-5 处理后的一景遥感影像
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.32
- Caption: 表 2-4 无人机影像精度验证
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 12
- Source anchor: p.35
- Caption: 表 3-1 遥感影像分类技术方法比较
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 13
- Source anchor: p.36
- Caption: 图 3-1 棋盘分割
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 14
- Source anchor: p.36
- Caption: 图 3-2 四叉树分割
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 15
- Source anchor: p.37
- Caption: 图 3-3 光谱差异分割
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 16
- Source anchor: p.39
- Caption: 图 4-4 棋盘分割
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 17
- Source anchor: p.39
- Caption: 图 4-5 四叉树分割
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 18
- Source anchor: p.39
- Caption: 图 4-6 光谱差异分割
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 19
- Source anchor: p.40
- Caption: 图 4-7 多尺度分割
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 20
- Source anchor: p.41
- Caption: 图 3-8 相同形状参数与紧致度参数下不同分割参数对比图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 21
- Source anchor: p.42
- Caption: 图 3-9 相同分割尺度与紧致度参数下不同形状参数对比图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 22
- Source anchor: p.42
- Caption: 图 3-10 相同分割尺度与形状参数下不同紧致度对比图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 23
- Source anchor: p.43
- Caption: 图 3-11 研究区 d 多尺度分割图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 24
- Source anchor: p.48
- Caption: 表 3-2 不同分类方法精度评价结果汇总
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 25
- Source anchor: p.48
- Caption: 图 3-12 对比三种方法对研究区 d 分类影像
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider


## 10. Results Reading Notes

- Source anchors: p.4, p.5, p.7, p.8, p.11, p.13, p.15, p.16, p.17, p.18, p.19, p.24, ...
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: 两个不同遥感影像数据进行对比验证计算结果的精确性。遥感影像数
- p.1: 提取裸岩信息的结果。结果表明，基于归一化岩石指数计算的基岩裸
- p.1: 岩石指数计算结果好于使用像元二分法 -植被覆盖度和土壤裸露率计
- p.1: 算岩石裸露率计算结果。两种裸岩信息提取结果对石漠化因子信息提
- p.1: 好； 在小尺度范围地区， 使用无人机航摄影像提取基岩裸露率 精度更
- p.2: 随着无人机技术的快速发展， 高精度的地表信息获取越来越方便
- p.2: 多尺度分割加隶属度分类得到结果具有更高精度、 提取岩石的信息更
- p.2: 准确， 结果面向对象分类结果精度达到 98%， 而其他分类精度提取结
- p.2: 果不高， 精度较低。而使用基于像元的光谱信息分类方法并没达到理
- p.3: accuracy of the calculation results.
- p.2: Study on Information extraction and Spatial
- p.2: Distribution Pattern of Rock in Rocky
- p.7: The change of landscape pattern has an important influence on the
- p.7: pattern in rocky desertification area fo r the development of rocky
- p.7: used to compare two different remote sensing image data to verify the
- p.7: accuracy of the calculation results.


## 11. Discussion Reading Notes

- Source anchors: not located
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.9: enlightenment to the future process of rocky desertification and the
- p.17: 利用覆盖进行分类， 探讨该方法在地物分类中的潜力和局限性。2006 年， 蒲智等
- p.29: 同时无人机技术依然存在一些局限性， 无人机影像在一些特殊的地形和地质
- p.34: 性加上遥感影像信息传递过程中的局限性决定了遥感影像信息传递的 不确定性
- p.34: 混合组成，如何提高分类精确性破除传统方法中的局限性是需要研究的问题。
- p.72: practitioners and future research[J].
- p.12: 6.总结与展望 ................................
- p.12: 6.2 存在不足及展望 ................................
- p.17: 利用覆盖进行分类， 探讨该方法在地物分类中的潜力和局限性。2006 年， 蒲智等
- p.29: 同时无人机技术依然存在一些局限性， 无人机影像在一些特殊的地形和地质
- p.29: 另外， 无人机图像采集时， 在弱光源下曝光不足， 导致图像较暗， 影响后期目标
- p.34: 性加上遥感影像信息传递过程中的局限性决定了遥感影像信息传递的 不确定性
- p.34: 混合组成，如何提高分类精确性破除传统方法中的局限性是需要研究的问题。
- p.35: 息不足以辨别地物， 甚至会造成相同光谱特性的不同地物错分为同一类， 因此使


## 12. Conclusion Reading Notes

- Source anchors: p.17, p.68
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: medium. Reason: grounded signals were located in the text layer.
- FBR/LSMM support: medium. Reason: grounded signals were located in the text layer.
- ML baseline support: medium. Reason: grounded signals were located in the text layer.
- semantic segmentation support: not applicable. Reason: grounded signals were not located in the text layer.
- DEM/topography support: not applicable. Reason: grounded signals were not located in the text layer.
- GF/Sentinel/Landsat data comparison support: medium. Reason: grounded signals were located in the text layer.
- cross-region transfer support: medium. Reason: grounded signals were located in the text layer.
- accuracy assessment support: medium. Reason: grounded signals were located in the text layer.
- Discussion comparison support: medium. Reason: grounded signals were located in the text layer.
- limitations support: medium. Reason: grounded signals were located in the text layer.
- figure/table design support: medium. Reason: grounded signals were located in the text layer.
- terminology support: medium. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: not applicable. Reason: grounded signals were not located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: bare_rock_fraction_fbr; unknown.
- Located target evidence pages: p.4, p.4, p.4, p.4, p.4, p.4.
- Located metric evidence pages: p.2, p.2, p.7, p.7, p.7, p.7.

### Writing patterns
- Use source-anchored Introduction gap statements and Methods reproducibility language; inspect the located Introduction/Methods pages before adopting exact wording.
- Pair map/accuracy figures with class-level metric tables when classification is involved.

### Terminology
- Canonical terms to preserve: karst rocky desertification; fractional bedrock/bare-rock fraction when explicitly used; LSMM/SMA/MESMA; OA/Kappa/F1/IoU for classification; R2/RMSE/MAE for continuous inversion.

### Warnings
- Do not treat LSMM continuous FBR output as a classification map.
- Do not compare R2/RMSE directly with OA/Kappa/F1/IoU as if they were the same metric type.
- Use spatially independent validation where possible; flag random patch split as a limitation.


## 15. Items Needing Manual Review

- DOI missing in database
- DOI needs manual verification
- metadata incomplete
