# Skin detection algorithm

A quick research on the internet shows that color segmentation is widely used for skin detection (specifically using HSV and YCbCr colorspaces), mostly by its simplicity and performance. However, skin tone, illumination, and quality are something that could drastically vary between images. For instance, [Kolkur et. al (2016)](https://arxiv.org/ftp/arxiv/papers/1708/1708.02694.pdf),  and [Sha et. al (2009)](https://www.researchgate.net/publication/221365117_Combinatorial_Color_Space_Models_for_Skin_Detection_in_Sub-continental_Human_Images) studied that kind of skin segmentation and discovered completely different optimal thresholds values.

Then, I decided to search for other methods and found this paper written by [Saxen and Al-Hamadi (2014)](https://www.researchgate.net/publication/267642008_COLOR-BASED_SKIN_SEGMENTATION_AN_EVALUATION_OF_THE_STATE_OF_THE_ART) which shows that region based gives a better output for skin detection tasks.

Here, a region-growing algorithm (Watershed) and a combination of HSV and YCbCr color segmentations work together to produce the output.

# How to use

This project was implemented using Python (3.10) and OpenCV (4.6). The class `SkinDetector`, available inside `skinDetector.py`, must be imported into your project and be used as follows:

```
    from src.skinDetector import SkinDetector

    detector = SkinDetector(image_path = "path/to/image")
    detector.find_skin()
    detector.show_all_images()
```

## Running:

### Linux

1. If you do not have python3 installed: `sudo apt-get install python3 python3-pip`

2. Go inside the project folder and run `pip3 install -r requeriments.txt`

3. Usage of the test app: `python3 app.py imageName`. For using the image inside the testImages use: `python3 app.py testImages/f2.jpg `


# Results (output)

![Screenshot1](https://i.imgur.com/9ulj5Fw.png)
![Screenshot2](https://i.imgur.com/iLMyYyc.png)
![Screenshot3](https://i.imgur.com/lnoUDpe.png)