# Projects in Data Science (2025)

The main purpose of given assignment is to classify skin lessions. Skin lesions are defined as areas of skin that visually differ from the surrounding tissue. They are relatively common and can develop from a variety of causes, including trauma, genetic factors, infection or autoimmune disorders. 

To support our analysis, we determine the number of hairs in each image and preprocess the images by removing hairs to improve the visibility of the lesions. This preprocessing step enhances the accuracy of lesion identification and classification, helping to distinguish lesions associated with potential diseases from those caused by non-cancerous factors.

Additionally, we tested different parameters, such as varying kernel sizes, thresholds, and radii. Image 0410 was uploaded twice to illustrate this process. We do this because we want to check if lowering the threshold successfully removes smaller hairs.

 ## Background of the problem 

We analysed the result.csv dataset:
1. Count how many times each person voted for images with rankings 0, 1, or 2.
2. Check which are the most disagreed on pictures and then perform hair removal on them.

Observations:
1. Vote Counts for Each Person (0, 1, 2):

| Person | 0  | 1  | 2  |
|--------|----|----|----|
| Dara   | 68 | 79 | 53 |
| Marta  | 67 | 77 | 56 |
| Filip  | 76 | 72 | 52 |
| Philip | 58 | 78 | 64 |
| Maja   | 70 | 82 | 52 |

2. 

### Hair Segmentation Examples
Hair Segenation was conducted using the TELEA method, based on the template code from the lecture. Below are examples of visually successful and unsuccessful results:



### Good results
In order to analyze the process of hair removal, we choose an image "img_0410.png", as we all marked its hair level as 2, which implies a big amount of hair. We can see that hair on picture "img_0410.png", were removed almost scompletely for kernel= 25, however a limited amount of hair is still left in place of the darker sport. When we increase the kernel to , we can observe a complete succesful hair removal.

![Unprocessed Image_0410](../data/img_0410.png)
![Processed Image_0410](processed_images/img_0410_processed.png)


### Bad results
However, the results are not as satisfactionary on image "img_0414.jpg", where also a significant amount of hair is present [hair level= 2 marked by all of us], as even though the hair was removed, the process left significant white spots in place of the hair. In contradiction to the former example, the hair on the image is white.

![Unprocessed Image_0414](../data/img_0414.png)
![Processed Image_0414](processed_images/img_0414_processed.png)
 















