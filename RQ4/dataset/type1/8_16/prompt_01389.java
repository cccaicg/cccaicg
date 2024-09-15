/**
 * @param environment
 * @param environment
 * @param arguments
 * @param options
 */
public CommandConfigImpl(Environment environment, String name,
        List<String> arguments, Map<Option, String> options) 
{
    this.environment = environment;
    this.name = name;
    this.arguments = arguments;
    this.options = options;
}       