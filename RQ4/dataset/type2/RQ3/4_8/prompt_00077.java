// LOAD/UPDATE PIXELS
public void loadPixels() 
{
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            pixels[i][j] = new Pixel(i, j);
        }
    }
}   