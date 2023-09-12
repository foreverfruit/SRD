# SRD
the official repository of the paper "Remote Sensing Image Haze Removal Based on Superpixel"

The presence of haze significantly degrades the quality of remote sensing images, resulting in issues such as color distortion, reduced contrast, loss of texture, and blurred image edges, which can ultimately lead to the failure of remote sensing application systems. In this paper, we propose a Superpixel-based visible Remote sensing image Dehazing algorithm, namely SRD. To begin, the remote sensing haze images are divided into content-aware patches using superpixels, which cluster adjacent pixels considering their similarities in color and brightness. We assume that each superpixel region shares the same atmospheric light and transmission properties. Subsequently, methods to estimate local atmospheric light and transmission within each superpixel are proposed. Unlike existing dehazing algorithms that assume a globally constant atmospheric light, our approach considers the global heterogeneous distribution of the atmospheric ambient light, which allows us to model it as a global non-uniform variable. Furthermore, we introduce an effective atmospheric light estimation method inspired by the maximum reflectance prior. Moreover, recognizing the wavelength-dependent nature of light transmission, we independently estimate the transmittance for each RGB channel of the input image. The quantitative and qualitative evaluation results of comprehensive experiments on synthetic datasets and real-world samples demonstrate the superior performance of the proposed algorithm compared to state-of-the-art methods for remote sensing image dehazing.

<center>
<img src="./img/SRD.png" alt="SRD" />
</center>


**The source code of the proposed SRD method will be released soon**...
