# Voxceleb-Fairness

This is the Github repository to support the paper "Improving Fairness in Speaker Verification Models Via Embedding Adaptation and Score Fusion".

The repo includes the Voxceleb-Fairness datasets and key experimental results.

### Voxceleb-Fairness Datasets

The <strong>VoxCeleb2-GRC</strong>(Gender Ratio Controlled) training dataset has five subsets. They have the same total of 2,500 speakers but with different numbers of male and female speakers. The female-to-male (F:M) gender ratio ranges from 9:1 to 1:9.

The <strong>VoxCeleb1-F</strong>(Fairness) test dataset controls for the presence of positive and negative trials with same or different genders.

The <strong>VoxCeleb1-F</strong> (Fairness-Hard) test dataset controls more strictly, in which it only contains the same gender positive and negative trails.


 <!-- {border-collapse:collapse;border-spacing:0;} -->
 <!-- border-color:black;border-style:solid;border-width:1px; -->
 <!-- border-color:black;border-style:solid;border-width:1px; -->
 
<style type="text/css">
.tg 
.tg td{font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:center;vertical-align:top}
</style>

<table class="tg" style="width: 100%">
<thead>
  <tr>
    <th class="tg-fymr">Gender   Trials</th>
    <th class="tg-fymr">Trial Count</th>
    <th class="tg-fymr" colspan="3">VoxCeleb1-F </th>
    <th class="tg-fymr" colspan="3">VoxCeleb1-FH </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-fymr" style="width: 10%;">[F]</td>
    <td class="tg-fymr" style="width: 10%;">[M]</td>
    <td class="tg-fymr" style="width: 10%;">[All]</td>
    <td class="tg-fymr" style="width: 10%;">[F]</td>
    <td class="tg-fymr" style="width: 10%;">[M]</td>
    <td class="tg-fymr" >[All]</td>
  </tr>
  <tr>
    <td class="tg-fymr">Positive F-F</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
  </tr>
  <tr>
    <td class="tg-fymr">Negative F-F</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
  </tr>
  <tr>
    <td class="tg-fymr">Negative M-F</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-fymr">Positive M-M</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
  </tr>
  <tr>
    <td class="tg-fymr">Negative M-M</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
  </tr>
</tbody>
</table>



### Experimental Results 


The supportive table for Figure 2 in the paper.


|          |  |  F9M1    |      |  |  F4M1    |      |  |   F1M1   |      |  |   F1M4   |      |  |  F1M9    |      |
|----------|------|------|------|------|------|------|------|------|------|------|------|------|:----:|:----:|:----:|
|          | Q/RN | H/RN |  <strong>GFN</strong> | Q/RN | H/RN |  <strong>GFN</strong> | Q/RN | H/RN |  <strong>GFN</strong>  | Q/RN | H/RN |  <strong>GFN</strong>  | Q/RN | H/RN |  <strong>GFN</strong>  |
|  <strong>EER[F]  | 3.52 | 3.35 | <strong>3.12 | 3.48 | 3.63 | <strong>3.07 | 4.15 | 3.80 | <strong>3.65 | 5.61 | 5.42 | <strong>4.92 | 6.51 | 6.25 | <strong>5.53 |
|  <strong>EER[M]  | 7.22 | 6.81 | <strong>5.88 | 5.71 | 5.49 | <strong>5.12 | 4.27 | 4.07 | <strong>4.00 | 3.65 | 3.65 | <strong>3.82 | 3.57 | 3.42 | <strong>3.30 |
| <strong>EER[All] | 6.78 | 6.46 | <strong>5.84 | 5.38 | 5.36 | <strong>4.80 | 4.98 | 4.65 | <strong>4.42 | 5.84 | 5.84 | <strong>5.04 | 7.11 | 7.15 | <strong>5.08 |
|    <strong>DS    | 3.70 | 3.46 | <strong>2.76 | 2.23 | 1.86 | <strong>2.05 | 0.12 | 0.27 | <strong>0.35 | 1.96 | 1.77 | <strong>1.10 | 2.94 | 2.83 | <strong>2.23 |



The supportive table for Figure 4 in the paper.


|          	|       	|       	|  <strong>F9M1 	|      	|      	|      	|       	|  <strong>F1M1 	|      	|      	|      	|       	|  <strong>F1M9 	|      	|      	|
|----------	|:-----:	|:-----:	|:-----:	|:----:	|:----:	|:----:	|:-----:	|:-----:	|:----:	|:----:	|:----:	|:-----:	|:-----:	|:----:	|:----:	|
|          	|  GBWL 	|  F-FT 	|  M-FT 	|  ES  	|  <strong>GFN 	| GBWL 	|  F-FT 	|  M-FT 	|  ES  	|  <strong>GFN 	| GBWL 	|  F-FT 	|  M-FT 	|  ES  	|  <strong>GFN 	|
| EER[F]   	|  9.07 	|  3.65 	|  9.32 	| 3.83 	| <strong>3.12 	| 4.86 	|  4.69 	| 12.34 	| 4.51 	| <strong>3.65 	| 6.95 	|  6.12 	| 12.25 	| 6.48 	| <strong>5.53 	|
| EER[M]   	|  8.03 	| 10.65 	|  6.78 	| 6.40 	| <strong>5.88 	| 7.67 	| 11.42 	|  5.81 	| 4.64 	| <strong>4.00 	| 8.95 	|  8.83 	|  4.12 	| 3.63 	| <strong>3.30 	|
| EER[All] 	| 13.38 	| 10.63 	| 15.63 	| 5.91 	| <strong>5.84 	| 9.47 	| 11.46 	| 15.39 	| 5.47 	| <strong>4.42 	| 9.88 	| 12.13 	| 13.42 	| 6.14 	| <strong>5.08 	|
| DS       	|  1.04 	|  7.00 	|  2.54 	| 2.57 	| <strong>2.76 	| 2.99 	|  6.73 	|  7.16 	| 0.31 	| <strong>0.35 	| 2.00 	|  2.71 	|  8.13 	| 2.85 	| <strong>2.23 	|