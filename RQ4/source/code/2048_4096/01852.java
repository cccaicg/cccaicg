/**
 * Allows to send an update packet when the team is built.
 *
 * @return this builder, for chaining
 */
public TeamBuilder updateTeamPacket(){
    this.updateTeam = true;
    return this;
}