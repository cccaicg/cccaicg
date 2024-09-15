//Note that the player killed something
public void kill(Player attacker, LivingEntity victim) 
{
    if (victim instanceof Player)
    {
        Player playerVictim = (Player)victim;
        if (playerVictim.getHealth() - attacker.getDamage() <= 0)
        {
            attacker.setScore(attacker.getScore() + 1);
        }
    }
}   