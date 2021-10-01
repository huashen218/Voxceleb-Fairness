# Voxceleb-Fairness

This is the Github repository to support the paper <a href="">"Improving fairness in speaker verification via Group-adapted Fusion Network"</a>.

The repo includes the Voxceleb-Fairness datasets and key experimental results.

### Voxceleb-Fairness Datasets

The <strong>VoxCeleb2-GRC</strong>(Gender Ratio Controlled) training dataset has five subsets. They have the same total of 2,500 speakers but with different numbers of male and female speakers. The female-to-male (F:M) gender ratio ranges from 9:1 to 1:9.

The <strong>VoxCeleb1-F</strong>(Fairness) test dataset controls for the presence of positive and negative trials with same or different genders.

The <strong>VoxCeleb1-FH</strong> (Fairness-Hard) test dataset controls more strictly, in which it only contains the same gender positive and negative trails.

<!-- 
<style type="text/css">
.tg {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:center;vertical-align:top}
</style> -->

<table class="tg" style="width: 100%; text-align:center;" >
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
    <td class="tg-fymr" style="width: 10%;">[All]</td>
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

<!-- <style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-bobw{font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-8d8j{text-align:center;vertical-align:bottom}
</style> -->

<table class="tg" style="width: 100%; text-align:center;" >
<thead>
  <tr>
    <th class="tg-8d8j"></th>
    <th class="tg-bobw" colspan="3">F9M1</th>
    <th class="tg-bobw" colspan="3">F4M1</th>
    <th class="tg-bobw" colspan="3">F1M1</th>
    <th class="tg-bobw" colspan="3">F1M4</th>
    <th class="tg-bobw" colspan="3">F1M9</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-8d8j"></td>
    <td class="tg-8d8j">Q/RN</td>
    <td class="tg-8d8j">H/RN</td>
    <td class="tg-8d8j">GFN</td>
    <td class="tg-8d8j">Q/RN</td>
    <td class="tg-8d8j">H/RN</td>
    <td class="tg-8d8j">GFN</td>
    <td class="tg-8d8j">Q/RN</td>
    <td class="tg-8d8j">H/RN</td>
    <td class="tg-8d8j">GFN</td>
    <td class="tg-8d8j">Q/RN</td>
    <td class="tg-8d8j">H/RN</td>
    <td class="tg-8d8j">GFN</td>
    <td class="tg-8d8j">Q/RN</td>
    <td class="tg-8d8j">H/RN</td>
    <td class="tg-8d8j">GFN</td>
  </tr>
  <tr>
    <td class="tg-bobw"><strong>EER[F]</td>
    <td class="tg-8d8j">3.52</td>
    <td class="tg-8d8j">3.35</td>
    <td class="tg-8d8j">3.12<br>(-11.36%)</td>
    <td class="tg-8d8j">3.48</td>
    <td class="tg-8d8j">3.63</td>
    <td class="tg-8d8j">3.07 <br>(-11.78%)</td>
    <td class="tg-8d8j">4.15</td>
    <td class="tg-8d8j">3.8</td>
    <td class="tg-8d8j">3.65 <br>(-12.05%)</td>
    <td class="tg-8d8j">5.61</td>
    <td class="tg-8d8j">5.42</td>
    <td class="tg-8d8j">4.92 <br>(-12.30%)</td>
    <td class="tg-8d8j">6.51</td>
    <td class="tg-8d8j">6.25</td>
    <td class="tg-8d8j">5.53 <br>(-15.05%)</td>
  </tr>
  <tr>
    <td class="tg-bobw"><strong>EER[M]</td>
    <td class="tg-8d8j">7.22</td>
    <td class="tg-8d8j">6.81</td>
    <td class="tg-8d8j">5.88<br>(-18.56%)</td>
    <td class="tg-8d8j">5.71</td>
    <td class="tg-8d8j">5.49</td>
    <td class="tg-8d8j">5.12 <br>(-10.33%)</td>
    <td class="tg-8d8j">4.27</td>
    <td class="tg-8d8j">4.07</td>
    <td class="tg-8d8j">4.00 <br>(-6.32%)</td>
    <td class="tg-8d8j">3.9</td>
    <td class="tg-8d8j">3.65</td>
    <td class="tg-8d8j">3.82 <br>(-2.05%)</td>
    <td class="tg-8d8j">3.57</td>
    <td class="tg-8d8j">3.42</td>
    <td class="tg-8d8j">3.30 <br>(-7.56%)</td>
  </tr>
  <tr>
    <td class="tg-bobw"><strong>EER[All]</td>
    <td class="tg-8d8j">6.78</td>
    <td class="tg-8d8j">6.46</td>
    <td class="tg-8d8j">5.84 <br>(-13.86%)</td>
    <td class="tg-8d8j">5.38</td>
    <td class="tg-8d8j">5.36</td>
    <td class="tg-8d8j">4.80 <br>(-10.78%)</td>
    <td class="tg-8d8j">4.98</td>
    <td class="tg-8d8j">4.65</td>
    <td class="tg-8d8j">4.42 <br>(-11.24%)</td>
    <td class="tg-8d8j">6.33</td>
    <td class="tg-8d8j">5.84</td>
    <td class="tg-8d8j">5.04 <br>(-20.38%)</td>
    <td class="tg-8d8j">7.11</td>
    <td class="tg-8d8j">7.15</td>
    <td class="tg-8d8j">5.08 <br>(-28.55%)</td>
  </tr>
  <tr>
    <td class="tg-bobw"><strong>DS</td>
    <td class="tg-8d8j">3.70</td>
    <td class="tg-8d8j">3.46</td>
    <td class="tg-8d8j">2.76 <br>(-25.41%)</td>
    <td class="tg-8d8j">2.23</td>
    <td class="tg-8d8j">1.86</td>
    <td class="tg-8d8j">2.05 <br>(-8.07%)</td>
    <td class="tg-8d8j">0.12</td>
    <td class="tg-8d8j">0.27</td>
    <td class="tg-8d8j">0.35 <br>(191.67%)</td>
    <td class="tg-8d8j">1.71</td>
    <td class="tg-8d8j">1.77</td>
    <td class="tg-8d8j">1.10 <br>(-35.67%)</td>
    <td class="tg-8d8j">2.94</td>
    <td class="tg-8d8j">2.83</td>
    <td class="tg-8d8j">2.23 <br>(-24.15%)</td>
  </tr>
</tbody>
</table>

The supportive table for Figure 4 in the paper.

<!-- <style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
.tg .tg-wa1i{font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-nrix{text-align:center;vertical-align:middle}
.tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
</style> -->

<table class="tg" style="width: 100%; text-align:center;" >
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
    <td class="tg-cly1"><strong>EER[F]</td>
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
    <td class="tg-cly1"><strong>EER[M]</td>
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
    <td class="tg-cly1"><strong>EER[All]</td>
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
    <td class="tg-cly1"><strong>DS</td>
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