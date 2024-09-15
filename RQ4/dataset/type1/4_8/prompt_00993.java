/*
 * (non-Javadoc)
 * @see org.eclipse.ui.plugin.AbstractUIPlugin#stop(org.osgi.framework.BundleContext)
 */
public void stop(BundleContext context) throws Exception 
{
    plugin = null;
    super.stop(context);
}   