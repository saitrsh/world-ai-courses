# Cambridge AI (Tripos Part IB) 真卷 · 逐份題型索引

> 對 `out/exams/cambridge/` 的 **21 份** past papers 逐份分類(2026-08-25 建)。
> 來源:[Cambridge CST past papers — Artificial Intelligence](https://www.cl.cam.ac.uk/teaching/exams/pastpapers/t-ArtificialIntelligence.html)(1993 起全公開)。
> 每份標主題、子題拆解與配分,末段給**題型頻率統計**與**對 NYCU 資格考 AI 卷的對照**。
> 出題者代號 **SBH / sbh11** = Sean Holden(近十年 AI I 命題者),故題風高度一致、可預測。

## 逐份索引

| 檔案 | 年份·卷 | 主題大類 | 子題型(配分) | 形式 |
|---|---|---|---|---|
| `y2004p5q6.pdf` | 2004 P5Q6 | **搜尋 / A\*** | 問題表示(5)· 完備/最佳性定義(2)· admissible/monotonic 定義(2)· A\* 運作(5)· **A\* 最佳性證明**(6) | 定義＋證明 |
| `y2017p4q1.pdf` | 2017 P4Q1 | **規劃(state-variable)＋CSP** | CSP 定義(4)· 一般→二元約束(3)· state-variable 表示(5)· 狀態表示(2)· 規劃→CSP 翻譯(6) | 定義＋建模 |
| `y2017p4q2.pdf` | 2017 P4Q2 | **神經網路 / 反向傳播** | 輸出節點梯度(線性,3)· sigmoid+交叉熵梯度(7)· **一般 δ 推導**(10) | 數學推導 |
| `y2018p6q1.pdf` | 2018 P6Q1 | **規劃 as SAT** | 滑塊→SAT(起始/目標 4·後繼狀態公理 4·前提公理 2·動作互斥 3·SAT-solver 演算法 3)· 用 local search 解 SAT(4) | 建模＋演算法 |
| `y2018p6q2.pdf` | 2018 P6Q2 | **神經網路 / CNN 反傳** | 視覺系統 ∂E/∂w 推導(12)· 卷積核修改後更新(8) | 數學推導 |
| `y2019p6q1.pdf` | 2019 P6Q1 | **規劃圖 / GraphPlan** | 積木→規劃問題(5)· 畫規劃圖(4)· 互斥:inconsistent effects/interfering actions(4)· competing preconditions(2)· 層數估計(2)· 長積木擴充難點(3) | 畫圖＋概念 |
| `y2019p6q2.pdf` | 2019 P6Q2 | **規劃(state-variable)＋啟發搜尋** | rigid relation/actions/state/goals(各2)· 啟發搜尋解規劃(3)· 與 CSP 比較(5)· admissible 啟發式＋證明(4) | 概念＋證明 |
| `y2020p6q1.pdf` | 2020 P6Q1 | **神經網路 / 反傳＋RBF** | 隱藏節點反傳(8)· **RBF 節點訓練演算法推導**(12) | 數學推導 |
| `y2020p6q2.pdf` | 2020 P6Q2 | **CSP** | 二元約束表示(4)· forward checking(4)· **AC-3 演算法**(6)· 施加一致性追蹤(6) | 演算法追蹤 |
| `y2021p6q1.pdf` | 2021 P6Q1 | **ML(線性迴歸)＋搜尋** | 線性迴歸梯度下降(5)· \|\|w\|\|≈1 正則化(5)· 啟發搜尋組件(4)· 用 ML 學啟發式(6) | 推導＋概念 |
| `y2021p6q2.pdf` | 2021 P6Q2 | **CSP / SAT** | CSP 描述(3)· SAT(CNF)→CSP(3)· 一般→二元約束(4)· forward checking(3)· FC 追蹤(5)· 傳播更廣影響(2) | 建模＋追蹤 |
| `y2022p6q1.pdf` | 2022 P6Q1 | **規劃圖 / GraphPlan** | 畫規劃圖至 S2(3)· 何時可抽取計畫(1+2)· 畫 Si-1/Ai-1/Si(4)· 標 4 種互斥(6)· 抽計畫 as 啟發搜尋(4) | 畫圖＋概念 |
| `y2022p6q2.pdf` | 2022 P6Q2 | **神經網路 / 反向傳播** | 權重共享 MLP:δ=σ'(a)∂E/∂y(3)· 輸出節點偏導(5)· 隱藏節點 δi(5)· 隱藏參數偏導(7) | 數學推導 |
| `y2023p7q1.pdf` | 2023 P7Q1 | **規劃(state-variable)＋CSP** | 迷宮:domain/rigid relation/function/goal(1+2+3+1)· 動作實作(6)· 轉 CSP(7) | 建模 |
| `y2023p7q2.pdf` | 2023 P7Q2 | **神經網路 / softmax 分類** | softmax 動機(4)· 交叉熵目標推導(6)· 反傳到 E(w) 的額外步驟(10) | 數學推導 |
| `y2024p7q1.pdf` | 2024 P7Q1 | **ML / 邏輯斯迴歸分類** | θ 的角色(1)· 改 activation 適應帶狀資料(6)· 交叉熵梯度下降＋明確公式(13) | 推導＋建模 |
| `y2024p7q2.pdf` | 2024 P7Q2 | **規劃 / 偏序規劃(POP)** | ordering constraint vs causal link(2+2)· 起始/結束態表示(3)· 動作表示(7)· promotion/demotion(6) | 概念＋建模 |
| `y2025p7q1.pdf` | 2025 P7Q1 | **搜尋(啟發式)＋ML** | heuristic 定義＋admissible(3)· **凸組合 admissible 證明**(2)· 監督式學啟發式(3)· 誤差函數批判(2)· 更好誤差(4)· 梯度下降推導(6) | 證明＋推導 |
| `y2025p7q2.pdf` | 2025 P7Q2 | **規劃(state-variable)** | 3D 洞穴:state-variable 元素(5)· 陷阱/鑰匙/越獄表示(5)· rigid relation 得 4 動作(5)· goRight 轉 CSP(5) | 建模 |
| `y2026p7q1.pdf` | 2026 P7Q1 | **CSP** | CSP 組件＋解(4)· V6 可否賦值(1)· forward checking 概念(2)· FC 追蹤序列 S(4)· 更早發現失敗(3)· **graph-based backjumping**(2+4) | 概念＋追蹤 |
| `y2026p7q2.pdf` | 2026 P7Q2 | **ML(線性迴歸)＋RBF** | 符號約束 via 正則化(4)· via 改 hw(x)(4)· 何者較佳(2)· MLP vs RBF 差異(2)· **RBF 梯度修改**(8) | 推導＋概念 |

## 題型頻率統計(21 份)

| 主題大類 | 出現份數 | 佔比 | 代表卷 |
|---|---|---|---|
| **神經網路 / 反向傳播**(含 CNN/RBF/softmax) | 6 | 29% | 2017P4Q2, 2018P6Q2, 2020P6Q1, 2022P6Q2, 2023P7Q2, 2026P7Q2 |
| **規劃**(state-variable / GraphPlan / SAT / POP) | 8 | 38% | 2017P4Q1, 2018P6Q1, 2019P6(Q1Q2), 2022P6Q1, 2023P7Q1, 2024P7Q2, 2025P7Q2 |
| **CSP**(forward checking / AC-3 / backjumping) | 6 | 29% | 2017P4Q1, 2020P6Q2, 2021P6Q2, 2023P7Q1, 2025P7Q2, 2026P7Q1 |
| **搜尋 / 啟發式**(A\* / admissible / 證明) | 4 | 19% | 2004P5Q6, 2019P6Q2, 2021P6Q1, 2025P7Q1 |
| **ML(非神經)**(線性/邏輯斯迴歸、梯度下降) | 5 | 24% | 2021P6Q1, 2024P7Q1, 2025P7Q1, 2026P7Q2 |

> 註:一份卷常橫跨 2 大類(如規劃常接 CSP、搜尋常接 ML),故佔比加總 >100%。

### 三條穩定命題主軸(近十年 sbh11)
1. **規劃 ⇄ CSP/SAT 的互轉** — 幾乎每年一題。掌握 state-variable representation、planning graph(mutex 四型)、規劃→CSP/SAT 翻譯。
2. **神經網路反向傳播的**「**從頭推導 δ**」 — 每 1–2 年一題,變體為 CNN(2018)、weight-sharing(2022)、RBF(2020/2026)、softmax(2023)。必練純手推 δ 與 ∂E/∂w。
3. **CSP 一致性演算法** — forward checking 必考,進階到 AC-3(2020)、backjumping(2026)。要能**逐步追蹤**指定賦值序列。

## 對 NYCU 資格考 AI 卷的對照

| Cambridge 主軸 | 是否落在 NYCU 資格考 AI 範圍 | 練這批的價值 |
|---|---|---|
| 搜尋 / A\* / admissible 證明 | ✅ 核心 | **高** — 證明題風格與資格考申論一致 |
| CSP / forward checking / AC-3 | ✅ 核心 | **高** — 逐步追蹤訓練最有效 |
| 規劃(state-variable / GraphPlan) | ⚠️ 部分(視當年命題) | 中 — 建模思維可遷移 |
| 神經網路反傳手推 | ✅(AIMA ML 章 + DL) | **高** — 純手推 δ 是共同硬功 |
| 線性/邏輯斯迴歸梯度下降 | ✅ 核心 | **高** — 公式化梯度是必得分點 |

**一句話:** 這 21 份最該優先刷 **CSP 逐步追蹤**(2020P6Q2, 2021P6Q2, 2026P7Q1)、**A\*/admissible 證明**(2004P5Q6, 2025P7Q1)、**反傳手推**(2017P4Q2, 2022P6Q2) — 三者題風與 NYCU 資格考申論/證明最貼近,且答案有標準結構、好自評。

---
*生成:2026-08-25 · 21 份逐份分類 · 資料來源公開(Cambridge CST past papers),僅供個人備考。*
