## Linear Regression

### Dataset

This script generates synthetic data for apartment sizes and their corresponding costs. The data includes some random noise to simulate real-world variability in apartment pricing.


### Environment
Executalble environment are listed in requirements.txt

... or run the script


```sh
pip install pandas numpy matplotlib
```


#### Run

Apartment Cost Data Generator function The generated data is saved as a CSV file named apartment_cost_vs_size.csv.

To use the data generator, you can run the script dataset.py

```sh

    python dataset.py
'''    

The head generated data frame will be printed and saved in apartment_cost_vs_size.csv.

The output looks like as follows:

``` txt
$ python dataset.py
   Size       Cost
0   602  187033.32
1   935  309622.07
2  1360  461453.87
3   770  287483.98
4   606  246717.19
```


