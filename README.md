# Steam: Template Matching

The goal of this repository is to provide a Colab notebook to match a template with Steam store images.

![Expected results][wiki-cover]

## Usage

-   Run [`steam_template_matching.ipynb`][colab-notebook-template-matching]
[![Open In Colab][colab-badge]][colab-notebook-template-matching]

-   Alternatively, to apply template matching on a few selected images, run:

```bash
python main.py
```

## Results

```
Test image name: library_600x900_2x.jpg
Template scale: 0.5
Correlation score: 0.71
```

![Result with correlation score 0.71][wiki-A1]
![Zoom in][wiki-A2]

```
Test image name: EGS_SeveredSteel_GreylockStudio_S1_2560x1440-7563487f2c1135a79b72a4d2c198d544
Template scale: 1.0
Correlation score: 0.99
```

![Result with correlation score 0.99][wiki-B1]
![Zoom in][wiki-B2]

```
Test image name: logo.png
Template scale: 0.3
Correlation score: 0.82
```

![Result with correlation score 0.82][wiki-C1]
![Zoom in][wiki-C2]

```
Test image name: Copyof15days-day13-wrapped-desktop-carousel-image1_1920x1080-e51f44e53902838f18bae6d3b0f1687e
Template scale: 0.5
Correlation score: 0.78
```

![Result with correlation score 0.78][wiki-D1]
![Zoom in][wiki-D2]

[colab-notebook-template-matching]: <https://colab.research.google.com/github/woctezuma/steam-template-matching/blob/main/steam_template_matching.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
[wiki-cover]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_B1.jpg>
[wiki-A1]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_A1.jpg>
[wiki-A2]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_A2.jpg>
[wiki-B1]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_B1.jpg>
[wiki-B2]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_B2.jpg>
[wiki-C1]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_C1.jpg>
[wiki-C2]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_C2.jpg>
[wiki-D1]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_D1.jpg>
[wiki-D2]: <https://github.com/woctezuma/steam-template-matching/wiki/img/img_D2.jpg>
