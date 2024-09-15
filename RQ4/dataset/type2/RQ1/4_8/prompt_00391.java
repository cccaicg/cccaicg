/**
 * Set to true to make TestRun print out details of successful property 
 * tests, not just those that fail. E.g.:
 * 
 * <pre>new TestRun().setVerbose(true).runOn(SomeInvariants.class, 1000);</pre>
 */
public TestRun setVerbose(boolean b) 
{
    verbose = b;
    return this;
}   