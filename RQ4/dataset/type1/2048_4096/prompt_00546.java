/**
 * @attribute syn
 * @aspect MultiCatch
 * @declaredat /Users/eric/Documents/workspaces/clara-soot/JastAddJ/Java7Frontend/MultiCatch.jrag:35
 */
public boolean isVolatile() 
{
    ASTNode$State state = state();
    try {
        return getModifiers().isVolatile();
    } finally {
    }
}   