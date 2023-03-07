<h1 align="center">
CRIN: Rotation-Invariant Point Cloud Analysis and Rotation Estimation via Centrifugal Reference Frame
</h1>


<div align="center">
<h3>
<a href="https://yokinglou.github.io">Yujing Lou</a>, Zelin Ye, <a href="https://qq456cvb.github.io">Yang You</a>, Nianjuan Jiang, Jiangbo Lu, Weiming Wang, <a href="https://dmcv.sjtu.edu.cn/">Lizhuang Ma</a>, <a href="https://www.mvig.org/">Cewu Lu</a>
<br>
AAAI 2023 (<font color="#FF0000">Oral</font>)
<br>
<br>
<a href='https://arxiv.org/abs/2303.03101'>
  <img src='https://img.shields.io/badge/Arxiv-PDF-red?style=flat&logo=arxiv&logoColor=red' alt='Paper PDF'>
</a>
<a href='https://arxiv.org/pdf/2303.03101.pdf'>
  <img src='https://img.shields.io/badge/Paper-Page-green?style=flat&logo=googlechrome&logoColor=green' alt='Paper'>
</a>
<a href='#'>
  <img src='https://img.shields.io/badge/Project-Page-blue?style=flat&logo=googlechrome&logoColor=blue' alt='Project Page'>
</a>
<br>
</h3>
</div>

<p align='center'>
<img align="center" src='figs/pipeline.jpg' width='90%'> </img>
</p>
 
In this paper, we propose the CRIN, namely Centrifugal Rotation-Invariant Network. CRIN directly takes the coordinates of points as input and transforms local points into rotation-invariant representations via centrifugal reference frames. Aided by centrifugal reference frames, each point corresponds to a discrete rotation so that the information of rotations can be implicitly stored in point features. Unfortunately, discrete points are far from describing the whole rotation space. We further introduce a continuous distribution for 3D rotations based on points. Furthermore, we propose an attention-based down-sampling strategy to sample points invariant to rotations. A relation module is adopted at last for reinforcing the long-range dependencies between sampled points and predicts the anchor point for unsupervised rotation estimation. Extensive experiments show that our method achieves rotation invariance, accurately estimates the object rotation. Ablation studies validate the effectiveness of the network design.


## Code
Coming soon.

## Citation
If you find our work useful, please consider citing

```bibtex
@misc{lou2023crin,
      title={CRIN: Rotation-Invariant Point Cloud Analysis and Rotation Estimation via Centrifugal Reference Frame}, 
      author={Yujing Lou and Zelin Ye and Yang You and Nianjuan Jiang and Jiangbo Lu and Weiming Wang and Lizhuang Ma and Cewu Lu},
      year={2023},
      eprint={2303.03101},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
