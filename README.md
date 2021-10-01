# Voxceleb-Fairness

This is the Github repository to support the paper "Improving Fairness in Speaker Verification Models Via Embedding Adaptation and Score Fusion".

The repo includes the Voxceleb-Fairness datasets and key experimental results.

### Voxceleb-Fairness Datasets

The <strong>VoxCeleb2-GRC</strong>(Gender Ratio Controlled) training dataset has five subsets. They have the same total of 2,500 speakers but with different numbers of male and female speakers. The female-to-male (F:M) gender ratio ranges from 9:1 to 1:9.

The <strong>VoxCeleb1-F</strong>(Fairness) test dataset controls for the presence of positive and negative trials with same or different genders.

The <strong>VoxCeleb1-F</strong> (Fairness-Hard) test dataset controls more strictly, in which it only contains the same gender positive and negative trails.

<!-- 
<style type="text/css">
.tg {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:center;vertical-align:top}
</style> -->

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
    <td class="tg-fymr"><strong>Positive F-F</strong></td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
  </tr>
  <tr>
    <td class="tg-fymr"><strong>Negative F-F</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
  </tr>
  <tr>
    <td class="tg-fymr"><strong>Negative M-F</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-fymr"><strong>Positive M-M</td>
    <td class="tg-0pky">150,000</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">✓</td>
    <td class="tg-0pky">✓</td>
  </tr>
  <tr>
    <td class="tg-fymr"><strong>Negative M-M</td>
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

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-l1d2{background-color:#FFF;color:#24292F;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-aldk{background-color:#FFF;color:#24292F;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-xao6{background-color:#FFF;color:#24292F;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-cwad{background-color:#FFF;color:#24292F;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-aldk"></th>
    <th class="tg-aldk" colspan="3"><span style="font-weight:600">F9M1</span></th>
    <th class="tg-aldk" colspan="3"><span style="font-weight:600">F4M1</span></th>
    <th class="tg-aldk" colspan="3"><span style="font-weight:600">F1M1</span></th>
    <th class="tg-aldk" colspan="3"><span style="font-weight:600">F1M4</span></th>
    <th class="tg-xao6" colspan="3"><span style="font-weight:600">F1M9</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-cwad"></td>
    <td class="tg-cwad">Q/RN</td>
    <td class="tg-cwad">H/RN</td>
    <td class="tg-l1d2"><span style="font-weight:600">GFN</span></td>
    <td class="tg-cwad">Q/RN</td>
    <td class="tg-cwad">H/RN</td>
    <td class="tg-l1d2"><span style="font-weight:600">GFN</span></td>
    <td class="tg-cwad">Q/RN</td>
    <td class="tg-cwad">H/RN</td>
    <td class="tg-l1d2"><span style="font-weight:600">GFN</span></td>
    <td class="tg-cwad">Q/RN</td>
    <td class="tg-cwad">H/RN</td>
    <td class="tg-l1d2"><span style="font-weight:600">GFN</span></td>
    <td class="tg-cwad">Q/RN</td>
    <td class="tg-cwad">H/RN</td>
    <td class="tg-l1d2"><span style="font-weight:600">GFN</span></td>
  </tr>
  <tr>
    <td class="tg-l1d2"><span style="font-weight:600">EER[F]</span></td>
    <td class="tg-cwad">3.52</td>
    <td class="tg-cwad">3.35</td>
    <td class="tg-l1d2"><span style="font-weight:600">3.12</span></td>
    <td class="tg-cwad">3.48</td>
    <td class="tg-cwad">3.63</td>
    <td class="tg-l1d2"><span style="font-weight:600">3.07</span></td>
    <td class="tg-cwad">4.15</td>
    <td class="tg-cwad">3.80</td>
    <td class="tg-l1d2"><span style="font-weight:600">3.65</span></td>
    <td class="tg-cwad">5.61</td>
    <td class="tg-cwad">5.42</td>
    <td class="tg-l1d2"><span style="font-weight:600">4.92</span></td>
    <td class="tg-cwad">6.51</td>
    <td class="tg-cwad">6.25</td>
    <td class="tg-l1d2"><span style="font-weight:600">5.53</span></td>
  </tr>
  <tr>
    <td class="tg-l1d2"><span style="font-weight:600">EER[M]</span></td>
    <td class="tg-cwad">7.22</td>
    <td class="tg-cwad">6.81</td>
    <td class="tg-l1d2"><span style="font-weight:600">5.88</span></td>
    <td class="tg-cwad">5.71</td>
    <td class="tg-cwad">5.49</td>
    <td class="tg-l1d2"><span style="font-weight:600">5.12</span></td>
    <td class="tg-cwad">4.27</td>
    <td class="tg-cwad">4.07</td>
    <td class="tg-l1d2"><span style="font-weight:600">4.00</span></td>
    <td class="tg-cwad">3.65</td>
    <td class="tg-cwad">3.65</td>
    <td class="tg-l1d2"><span style="font-weight:600">3.82</span></td>
    <td class="tg-cwad">3.57</td>
    <td class="tg-cwad">3.42</td>
    <td class="tg-l1d2"><span style="font-weight:600">3.30</span></td>
  </tr>
  <tr>
    <td class="tg-l1d2"><span style="font-weight:600">EER[All]</span></td>
    <td class="tg-cwad">6.78</td>
    <td class="tg-cwad">6.46</td>
    <td class="tg-l1d2"><span style="font-weight:600">5.84</span></td>
    <td class="tg-cwad">5.38</td>
    <td class="tg-cwad">5.36</td>
    <td class="tg-l1d2"><span style="font-weight:600">4.80</span></td>
    <td class="tg-cwad">4.98</td>
    <td class="tg-cwad">4.65</td>
    <td class="tg-l1d2"><span style="font-weight:600">4.42</span></td>
    <td class="tg-cwad">5.84</td>
    <td class="tg-cwad">5.84</td>
    <td class="tg-l1d2"><span style="font-weight:600">5.04</span></td>
    <td class="tg-cwad">7.11</td>
    <td class="tg-cwad">7.15</td>
    <td class="tg-l1d2"><span style="font-weight:600">5.08</span></td>
  </tr>
  <tr>
    <td class="tg-l1d2"><span style="font-weight:600">DS</span></td>
    <td class="tg-cwad">3.70</td>
    <td class="tg-cwad">3.46</td>
    <td class="tg-l1d2"><span style="font-weight:600">2.76</span></td>
    <td class="tg-cwad">2.23</td>
    <td class="tg-cwad">1.86</td>
    <td class="tg-l1d2"><span style="font-weight:600">2.05</span></td>
    <td class="tg-cwad">0.12</td>
    <td class="tg-cwad">0.27</td>
    <td class="tg-l1d2"><span style="font-weight:600">0.35</span></td>
    <td class="tg-cwad">1.96</td>
    <td class="tg-cwad">1.77</td>
    <td class="tg-l1d2"><span style="font-weight:600">1.10</span></td>
    <td class="tg-cwad">2.94</td>
    <td class="tg-cwad">2.83</td>
    <td class="tg-l1d2"><span style="font-weight:600">2.23</span></td>
  </tr>
</tbody>
</table>


The supportive table for Figure 4 in the paper.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
.tg .tg-wa1i{font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-nrix{text-align:center;vertical-align:middle}
.tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-wa1i"></th>
    <th class="tg-wa1i" colspan="5">F9M1&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-wa1i" colspan="5">F1M1&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-wa1i" colspan="5">F1M9&nbsp;&nbsp;&nbsp;</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-cly1"></td>
    <td class="tg-nrix">GBWL</td>
    <td class="tg-nrix">F-FT</td>
    <td class="tg-nrix">M-FT</td>
    <td class="tg-nrix">ES</td>
    <td class="tg-amwm">GFN</td>
    <td class="tg-nrix">GBWL</td>
    <td class="tg-nrix">F-FT</td>
    <td class="tg-nrix">M-FT</td>
    <td class="tg-nrix">ES</td>
    <td class="tg-amwm">GFN</td>
    <td class="tg-nrix">GBWL</td>
    <td class="tg-nrix">F-FT</td>
    <td class="tg-nrix">M-FT</td>
    <td class="tg-nrix">ES</td>
    <td class="tg-amwm">GFN</td>
  </tr>
  <tr>
    <td class="tg-cly1">EER[F]</td>
    <td class="tg-nrix">9.07</td>
    <td class="tg-nrix">3.65</td>
    <td class="tg-nrix">9.32</td>
    <td class="tg-nrix">3.83</td>
    <td class="tg-amwm">3.12</td>
    <td class="tg-nrix">4.86</td>
    <td class="tg-nrix">4.69</td>
    <td class="tg-nrix">12.34</td>
    <td class="tg-nrix">4.51</td>
    <td class="tg-amwm">3.65</td>
    <td class="tg-nrix">6.95</td>
    <td class="tg-nrix">6.12</td>
    <td class="tg-nrix">12.25</td>
    <td class="tg-nrix">6.48</td>
    <td class="tg-amwm">5.53</td>
  </tr>
  <tr>
    <td class="tg-cly1">EER[M]</td>
    <td class="tg-nrix">8.03</td>
    <td class="tg-nrix">10.65</td>
    <td class="tg-nrix">6.78</td>
    <td class="tg-nrix">6.40</td>
    <td class="tg-amwm">5.88</td>
    <td class="tg-nrix">7.67</td>
    <td class="tg-nrix">11.42</td>
    <td class="tg-nrix">5.81</td>
    <td class="tg-nrix">4.64</td>
    <td class="tg-amwm">4.00</td>
    <td class="tg-nrix">8.95</td>
    <td class="tg-nrix">8.83</td>
    <td class="tg-nrix">4.12</td>
    <td class="tg-nrix">3.63</td>
    <td class="tg-amwm">3.30</td>
  </tr>
  <tr>
    <td class="tg-cly1">EER[All]</td>
    <td class="tg-nrix">13.38</td>
    <td class="tg-nrix">10.63</td>
    <td class="tg-nrix">15.63</td>
    <td class="tg-nrix">5.91</td>
    <td class="tg-amwm">5.84</td>
    <td class="tg-nrix">9.47</td>
    <td class="tg-nrix">11.46</td>
    <td class="tg-nrix">15.39</td>
    <td class="tg-nrix">5.47</td>
    <td class="tg-amwm">4.42</td>
    <td class="tg-nrix">9.88</td>
    <td class="tg-nrix">12.13</td>
    <td class="tg-nrix">13.42</td>
    <td class="tg-nrix">6.14</td>
    <td class="tg-amwm">5.08</td>
  </tr>
  <tr>
    <td class="tg-cly1">DS</td>
    <td class="tg-nrix">1.04</td>
    <td class="tg-nrix">7.00</td>
    <td class="tg-nrix">2.54</td>
    <td class="tg-nrix">2.57</td>
    <td class="tg-amwm">2.76</td>
    <td class="tg-nrix">2.99</td>
    <td class="tg-nrix">6.73</td>
    <td class="tg-nrix">7.16</td>
    <td class="tg-nrix">0.31</td>
    <td class="tg-amwm">0.35</td>
    <td class="tg-nrix">2.00</td>
    <td class="tg-nrix">2.71</td>
    <td class="tg-nrix">8.13</td>
    <td class="tg-nrix">2.85</td>
    <td class="tg-amwm">2.23</td>
  </tr>
</tbody>
</table>