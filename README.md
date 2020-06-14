MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language
============================================================================================

This package containing the `MS-ASL dataset`, as proposed in MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language paper.  
For more information visit [the website](https://www.microsoft.com/en-us/research/project/ms-asl/).

Contents
-----------------
The directory contains following files:

 * `MSASL_train.json`: includes a json file of 16054 train samples.

 * `MSASL_test.json`: includes a json file of 4172 test samples.

 * `MSASL_val.json`: includes a json file of 5287 validation samples.

 * `MSASL_classes.json`: includes a json file of 1000 glosses (words) representing classes in the classification task. The first word in the set (`hello`) is class 0 and the last world on the set (`challenge`) is class 999.

 * `MSASL_synonym.json`: each row is a list of words that we considered synonym and assign a single class for all of them.

 * `C-UDA-0.1_annotated_discussion.pdf`: the Computational Use of Data Agreement (C-UDA) lisense agreement.

 * `README.md`: this file.


Structure
-----------------
Here is the structure of each sample clip in Train, test or validation sets.


```
{
    'url': a url link to the video,
    'start_time': the starting point of the clip in the original video in seconds,
    'end_time': the ending point of the clip in the original video in seconds,
    'label': class (an integer between 0 to 999),
    'signer_id': the id of the signer,
    'box': the boudy bounding box of the signer such as [y0, x0, y1, x1] where (x0, y0) is up-left corner and (x1,y1) is bottom-right corner. All the values are normalized (between zero and one) according to width and height,
    'text': the gloss for this clip which match the 'label',
    'width': width for the original video,
    'height': height for the original video,
    'fps': frame per second for the original video
}
```

We are suggesting the width, height and fps because the labeling has been done based on them but since start and end are time base and box is normalize in theory this annotation works for arbitrary width, height and fps.


Subsets
---------------
As mention in the paper this dataset includes 4 subsets: MS-ASL100, MS-ASL200, MS-ASL500 and MS-ASL1000.
To obtain each of these subsets you need to filter the train, test and validation based on the 'label'. This means that for MS-ASL100 just keep the samples with 'label' less that 100.


Credits
---------------
Licensed under the Computational Use of Data Agreement (C-UDA). Please refer to [C-UDA-0.1_annotated_discussion.pdf](/C-UDA-0.1_annotated_discussion.pdf) for more information.


Citation
--------------

Please cite this in your publications if it help your research:

    `@InProceedings{vaezijoze2019ms-asl,
      author    = {Vaezi Joze, Hamid Reza and Koller, Oscar}
      title     = {MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language},
      booktitle = {The British Machine Vision Conference (BMVC)},
      year      = {2019},
      month = {September}
    }`


Contacts
------------------
- [Hamid Vaezi Joze](https://www.microsoft.com/en-us/research/people/hava/)
- [Oscar Koller](https://www.microsoft.com/en-us/research/people/oskoller/)