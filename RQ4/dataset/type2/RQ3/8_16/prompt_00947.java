/**
 * Computes the output values of the output nodes in the network given input
 * values.
 * 
 * @param input - The input values.
 * @return double[] The vector of computed output values
 */
public double[] feedForward(double[] input) 
{
    double[] output = new double[numOutputs];
    for (int i = 0; i < numOutputs; i++)
    {
        output[i] = outputs[i].compute(input);
    }
    return output;
}   