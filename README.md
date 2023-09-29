# SRD
the official repository of the paper "**Remote Sensing Image Haze Removal Based on Superpixel**"


<center>
<img src="./img/SRD.png" alt="SRD" />
</center>
<br/>
<p style="text-align:justify">The presence of haze significantly degrades the quality of remote sensing images, resulting in issues such as color distortion, reduced contrast, loss of texture, and blurred image edges, which can ultimately lead to the failure of remote sensing application systems. In this paper, we propose a superpixel-based visible remote sensing image dehazing algorithm, namely SRD. To begin, the remote sensing haze images are divided into content-aware patches using superpixels, which cluster adjacent pixels considering their similarities in color and brightness. We assume that each superpixel region shares the same atmospheric light and transmission properties. Subsequently, methods to estimate local atmospheric light and transmission within each superpixel are proposed. Unlike existing dehazing algorithms that assume a globally constant atmospheric light, our approach considers the global heterogeneous distribution of the atmospheric ambient light, which allows us to model it as a global non-uniform variable. Furthermore, we introduce an effective atmospheric light estimation method inspired by the maximum reflectance prior. Moreover, recognizing the wavelength-dependent nature of light transmission, we independently estimate the transmittance for each RGB channel of the input image. The quantitative and qualitative evaluation results of comprehensive experiments on synthetic datasets and real-world samples demonstrate the superior performance of the proposed algorithm compared to state-of-the-art methods for remote sensing image dehazing.</p>


## Citation

If you find our work useful in your research, please cite:

```tex
@article{he2023remote,
  title={Remote Sensing Image Haze Removal Based on Superpixel},
  author={He, Yufeng and Li, Cuili and Bai, Tiecheng},
  journal={Remote Sensing},
  volume={15},
  number={19},
  pages={4680},
  year={2023},
  publisher={MDPI}
}
```

https://doi.org/10.3390/rs15194680


## Results

<table>
<tr>
	<td>input<img src="./img/hazy/AID_railwaystation_22.jpg" width="100%" alt="input" /></td>
	<td>dehazed<img src="./img/result/AID_railwaystation_22.jpg" width="100%" alt="SRD" /></td>
</tr>
<tr>
	<td>superpixel_edge<img src="./img/result/AID_railwaystation_22_superpixel.jpg" width="100%" alt="input" /></td>
	<td>superpixel_embed<img src="./img/result/AID_railwaystation_22_embed.jpg" width="100%" alt="SRD" /></td>
    <td>Coarse A<img src="./img/result/AID_railwaystation_22_Acoarse.jpg" width="100%" alt="input" /></td>
	<td>Refined A<img src="./img/result/AID_railwaystation_22_Arefine.jpg" width="100%" alt="SRD" /></td>
</tr>
<tr>
	<td>Coarse T Red<img src="./img/result/AID_railwaystation_22_TR_coarse.jpg" width="100%" alt="SRD_TR_Coarse" /></td>
	<td>Coarse T Green<img src="./img/result/AID_railwaystation_22_TG_coarse.jpg" width="100%" alt="SRD_TG_Coarse" /></td>
     <td>Coarse T Blue<img src="./img/result/AID_railwaystation_22_TB_coarse.jpg" width="100%" alt="SRD_TB_Coarse" /></td>
</tr>
<tr>
<td>Refined T Red<img src="./img/result/AID_railwaystation_22_TR_refine.jpg" width="100%" alt="SRD_TR_refined" /></td>
	<td>Refined T Green<img src="./img/result/AID_railwaystation_22_TG_refine.jpg" width="100%" alt="SRD_TG_refined" /></td>
     <td>Refined T Blue<img src="./img/result/AID_railwaystation_22_TB_refine.jpg" width="100%" alt="SRD_TB_refined" /></td>
</tr>
</table>

<table>
<tr>
	<td>input<img src="./img/hazy/DIOR_TEST_13848.jpg" width="100%" alt="input" /></td>
	<td>dehazed<img src="./img/result/DIOR_TEST_13848.jpg" width="100%" alt="SRD" /></td>
</tr>
<tr>
	<td>superpixel_edge<img src="./img/result/DIOR_TEST_13848_superpixel.jpg" width="100%" alt="input" /></td>
	<td>superpixel_embed<img src="./img/result/DIOR_TEST_13848_embed.jpg" width="100%" alt="SRD" /></td>
    <td>Coarse A<img src="./img/result/DIOR_TEST_13848_Acoarse.jpg" width="100%" alt="input" /></td>
	<td>Refined A<img src="./img/result/DIOR_TEST_13848_Arefine.jpg" width="100%" alt="SRD" /></td>
</tr>
<tr>
	<td>Coarse T Red<img src="./img/result/DIOR_TEST_13848_TR_coarse.jpg" width="100%" alt="SRD_TR_Coarse" /></td>
	<td>Coarse T Green<img src="./img/result/DIOR_TEST_13848_TG_coarse.jpg" width="100%" alt="SRD_TG_Coarse" /></td>
     <td>Coarse T Blue<img src="./img/result/DIOR_TEST_13848_TB_coarse.jpg" width="100%" alt="SRD_TB_Coarse" /></td>
</tr>
<tr>
<td>Refined T Red<img src="./img/result/DIOR_TEST_13848_TR_refine.jpg" width="100%" alt="SRD_TR_refined" /></td>
	<td>Refined T Green<img src="./img/result/DIOR_TEST_13848_TG_refine.jpg" width="100%" alt="SRD_TG_refined" /></td>
     <td>Refined T Blue<img src="./img/result/DIOR_TEST_13848_TB_refine.jpg" width="100%" alt="SRD_TB_refined" /></td>
</tr>
</table>

<table>
<tr>
	<td>input<img src="./img/hazy/AID_industrial_107.jpg" width="100%" alt="input" /></td>
	<td>dehazed<img src="./img/result/AID_industrial_107.jpg" width="100%" alt="SRD" /></td>
</tr>
<tr>
	<td>superpixel_edge<img src="./img/result/AID_industrial_107_superpixel.jpg" width="100%" alt="input" /></td>
	<td>superpixel_embed<img src="./img/result/AID_industrial_107_embed.jpg" width="100%" alt="SRD" /></td>
    <td>Coarse A<img src="./img/result/AID_industrial_107_Acoarse.jpg" width="100%" alt="input" /></td>
	<td>Refined A<img src="./img/result/AID_industrial_107_Arefine.jpg" width="100%" alt="SRD" /></td>
</tr>
<tr>
	<td>Coarse T Red<img src="./img/result/AID_industrial_107_TR_coarse.jpg" width="100%" alt="SRD_TR_Coarse" /></td>
	<td>Coarse T Green<img src="./img/result/AID_industrial_107_TG_coarse.jpg" width="100%" alt="SRD_TG_Coarse" /></td>
     <td>Coarse T Blue<img src="./img/result/AID_industrial_107_TB_coarse.jpg" width="100%" alt="SRD_TB_Coarse" /></td>
</tr>
<tr>
<td>Refined T Red<img src="./img/result/AID_industrial_107_TR_refine.jpg" width="100%" alt="SRD_TR_refined" /></td>
	<td>Refined T Green<img src="./img/result/AID_industrial_107_TG_refine.jpg" width="100%" alt="SRD_TG_refined" /></td>
     <td>Refined T Blue<img src="./img/result/AID_industrial_107_TB_refine.jpg" width="100%" alt="SRD_TB_refined" /></td>
</tr>
</table>

## Acknowledgement

We thank the project  [fast-slic](https://github.com/Algy/fast-slic) for providing the implementations for the SLIC algorithm!





