// Return a list of all the planets owned by the current player. By
// convention, the current player is always player number 1.
public List<Planet> MyPlanets() 
{
    List<Planet> r = new ArrayList<Planet>();
    for (Planet p : Planets) {
        if (p.ownedBy() == 1) {
            r.add(p);
        }
    }
    return r;
}   