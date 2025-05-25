
package org.apache.commons.cli;

import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;


public class CommandLine {

    private List args = new LinkedList();

    private Map options = new HashMap();
    private Map names = new HashMap();

    private Map hashcodeMap = new HashMap();

    CommandLine()
    {
    }

    public boolean hasOption(String opt)
    {
        return options.containsKey(opt);
    }


    public boolean hasOption(char opt)
    {
        return hasOption(String.valueOf(opt));
    }

    public Object getOptionObject(String opt)
    {
        String res = getOptionValue(opt);

        if (!options.containsKey(opt))
        {
            return null;
        }

        Object type = ((Option) options.get(opt)).getType();

        return (res == null)        ? null : TypeHandler.createValue(res, type);
    }

    public Object getOptionObject(char opt)
    {
        return getOptionObject(String.valueOf(opt));
    }

    public String getOptionValue(String opt)
    {
        String[] values = getOptionValues(opt);

        return (values == null) ? null : values[0];
    }

    public String getOptionValue(char opt)
    {
        return getOptionValue(String.valueOf(opt));
    }

    public String[] getOptionValues(String opt)
    {
        opt = Util.stripLeadingHyphens(opt);

        String key = opt;
        if (names.containsKey(opt))
        {
            key = (String) names.get(opt);
        }
        if (options.containsKey(key))
        {
            return ((Option) options.get(key)).getValues();
        }

        return null;
        }

    public String[] getOptionValues(char opt)
    {
        return getOptionValues(String.valueOf(opt));
    }

    public String getOptionValue(String opt, String defaultValue)
    {
        String answer = getOptionValue(opt);

        return (answer != null) ? answer : defaultValue;
    }

    public String getOptionValue(char opt, String defaultValue)
    {
        return getOptionValue(String.valueOf(opt), defaultValue);
    }

    public String[] getArgs()
    {
        String[] answer = new String[args.size()];

        args.toArray(answer);

        return answer;
    }

    public List getArgList()
    {
        return args;
    }

    void addArg(String arg)
    {
        args.add(arg);
    }

    void addOption(Option opt)
    {
        hashcodeMap.put(new Integer(opt.hashCode()), opt);
        String key = opt.getKey();
        if (key == null)
        {
            key = opt.getLongOpt();
        }
        else
        {
            names.put(opt.getLongOpt(), key);
        }
        options.put(key, opt);
    }

    public Iterator iterator()
    {
        return hashcodeMap.values().iterator();
    }

    public Option[] getOptions()
    {
        Collection processed = options.values();
        Option[] optionsArray = new Option[processed.size()];
        return (Option[]) processed.toArray(optionsArray);
    }
}
