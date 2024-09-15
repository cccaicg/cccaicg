/**
 * @param donutClient
 * @param knownNode
 *            {@link TNode} on which to join.
 */
public DonutJoinClosure(DonutClient donutClient, TNode knownNode) 
{
    this.donutClient = donutClient;
    this.knownNode = knownNode;
}   