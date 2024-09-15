/**
 * еķѼϼ֪ʶϵͳ
 */
private ArrayList<RecordCollection> computeKnowledgeSystem(
		HashMap<String, ArrayList<RecordCollection>> collectionMap) 
{
	ArrayList<RecordCollection> knowledgeSystem = new ArrayList<RecordCollection>();
	for (String key : collectionMap.keySet())
	{
		knowledgeSystem.addAll(collectionMap.get(key));
	}
	return knowledgeSystem;
}	