/**
 * Returns a wild species for fishing
 * @return
 */
private String getWildSpeciesFish() 
{
    int i = random.nextInt(2);
    switch (i)
    {
        case 0:
            return "Salmon";
        case 1:
            return "Trout";
        default:
            return "Salmon";
    }
}   