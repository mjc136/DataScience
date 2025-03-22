# face recognition

## 13/03/2025
research into 
- https://github.com/microsoft/DigiFace1M
- https://www.tensorflow.org/tutorials/images/cnn

## 18/03/2025

created model and trained 32 subjects with 20 epochs to test if it works
getting accuracy of 85

adding 100 subjects made accuracy drop so have to do preprocessing

- added Data Augmentation
-

## 20/03/2025

adding more layers and epochs

tried EfficientNetB0 model instead of mobilenetv2 but its behaving poorly

## 21/03/2025

tried getting tensorflow to use gpu but wont work

tried changing batch size and it fixed the val accuraccy being terribly
got first successful prediction but i think it was a fluke

still having overfitting issue where as training loss gets lower val_loss gets higher

## 22/03/2025

trying large number of epochs with callbacks
got succesful prediction with 50 percent confidence