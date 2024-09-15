/**
 * Fixes the error by assigning the result of the call to the receiver reference, or deleting the
 * method call.
 */
private Description describe(MethodInvocationTree methodInvocationTree, VisitorState state) 
{
    ExpressionTree receiver = methodInvocationTree.getMethodSelect();
    if (receiver.getKind() == Tree.Kind.IDENTIFIER) {
        return describe((IdentifierTree)receiver, methodInvocationTree, state);
    }
    return describe(receiver, methodInvocationTree, state);
}   