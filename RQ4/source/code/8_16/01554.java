/**
 * Sets or resets allow mutate flag.
 * If this flag is set, then all automata operations may modify automata given as input;
 * otherwise, operations will always leave input automata languages unmodified. 
 * By default, the flag is not set.
 * @param flag if true, the flag is set
 * @return previous value of the flag
 */
static public boolean setAllowMutate(boolean flag){
	boolean b = allow_mutation;
	allow_mutation = flag;
	return b;
}