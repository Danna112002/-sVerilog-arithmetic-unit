#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double CalculateArithmeticMean(double value, double weight, double weightSum)
{
    double sum = 0.0;
    double arithMean = 0;

    sum = value * weight;

    arithMean = sum / weightSum;

    return arithMean;
}

double CalculateGeometricMean(double value, double weight, double weightSum)
{
    double product = 1.0;
    double geoMean = 1.0;
        
    product = pow(value, weight);
        
    geoMean = pow(product, 1.0 / weightSum);

    return geoMean; 
}


int GetNumPairs()
{
    int numPairs = 0;
    printf("Enter the number of pairs (50 or less):\n");
    scanf("%d", &numPairs);
    if (numPairs > 50 || numPairs <= 0) 
    {
        printf("Invalid input. Please enter a number between 1 and 50.\n");
        scanf("%d", &numPairs);
    }
    return numPairs;
}

int GetWeightSum(double array[][50], int numPairs)
{
    int weightSum = 0;

    for (int i = 0; i < numPairs; i++) 
    {
        weightSum += array[1][i];
    }

    return weightSum;
}


void ZeroArray(int numPairs, double array[][50])
{
    for (int i = 0; i < numPairs; i++) 
    {
        array[0][i] = 0;
        array[1][i] = 0;
    }
}

int main()
{
    int numPairs = 0;
    int weightSum = 0;
    double array[2][50];
    ZeroArray(numPairs, array);
    double arithMean = 0;
    double geoMean = 1.0;
    numPairs = GetNumPairs();
    for (int i = 0; i < numPairs; i++) 
        {
            printf("Enter a pair of numbers in the format (value weight), both followed by enter:\n");
            scanf("%lf %lf", &array[0][i], &array[1][i]);
        }

    weightSum = GetWeightSum(array, numPairs);
    for (int i = 0; i < numPairs; i++)
    { 
        arithMean += CalculateArithmeticMean(array[0][i], array[1][i], weightSum);
        geoMean *= CalculateGeometricMean(array[0][i], array[1][i], weightSum);
    }
    printf("The arithmetic mean of the data set is: %f\n", arithMean);
    printf("The geometric mean of the data set is: %f\n", geoMean);


    return 0;
}