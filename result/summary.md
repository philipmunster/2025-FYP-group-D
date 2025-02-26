# Projects in Data Science (2025)

The main purpose of given assignment is to classify skin lessions. Skin lesions are defined as areas of skin that visually differ from the surrounding tissue. They are relatively common and can develop from a variety of causes, including trauma, genetic factors, infection or autoimmune disorders. 

To support our analysis, we determine the number of hairs in each image and preprocess the images by removing hairs to improve the visibility of the lesions. This preprocessing step enhances the accuracy of lesion identification and classification, helping to distinguish lesions associated with potential diseases from those caused by non-cancerous factors.

Additionally, we tested different parameters, such as varying kernel sizes, thresholds, and radii. Image 0410 was uploaded twice to illustrate this process. We do this because we want to check if lowering the threshold successfully removes smaller hairs.

 ## Background of the problem 

We analysed the result.csv dataset:
1. Counted how many times each person voted for images with rankings 0, 1, or 2.
2. Checked when people agreed and disagreed with each other.
3. Plot relevant graphs for visual representation.

Observations:
1. Vote Counts for Each Person (0, 1, 2):

| Person | 0  | 1  | 2  |
|--------|----|----|----|
| Dara   | 68 | 79 | 53 |
| Marta  | 67 | 77 | 56 |
| Filip  | 76 | 72 | 52 |
| Philip | 58 | 78 | 64 |
| Maja   | 70 | 82 | 52 |

2. Looking through the data, one such picture where everyone agrees is:
    img_0393.png with rank 1 for all people.
    



### Hair Segmentation Examples
Hair Segenation was conducted using the TELEA method, based on the template code from the lecture. Below are examples of visually successful and unsuccessful results:



### Good results
We can see that hair on these pictures were removed successfully.

### Bad results
Here we can see that there is some remaining hair therefore poor visual results.








