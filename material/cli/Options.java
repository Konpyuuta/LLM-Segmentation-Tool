
package org.apache.commons.cli;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Options {

    private Map shortOpts = new HashMap();

    private Map longOpts = new HashMap();

    private List requiredOpts = new ArrayList();

    private Map optionGroups = new HashMap();

    public Options()
    {
    }

    public Options addOptionGroup(OptionGroup group)
    {
        Iterator options = group.getOptions().iterator();

        if (group.isRequired())
        {
            requiredOpts.add(group);
        }

        while (options.hasNext())
        {
            Option option = (Option) options.next();

            option.setRequired(false);
            addOption(option);

            optionGroups.put(option.getKey(), group);
        }

        return this;
    }

    Collection getOptionGroups(){
    	return new HashSet(optionGroups.values());
    }

    public Options addOption(String opt, boolean hasArg, String description)
    {
        addOption(opt, null, hasArg, description);

        return this;
    }

    public Options addOption(String opt, String longOpt, boolean hasArg, 
                             String description)
    {
        addOption(new Option(opt, longOpt, hasArg, description));

        return this;
    }

    public Options addOption(Option opt)
    {
        String key = opt.getKey();

        if (opt.hasLongOpt())
        {
            longOpts.put(opt.getLongOpt(), opt);
        }

        if (opt.isRequired() )
        {
            if( requiredOpts.contains(key) ) {
                requiredOpts.remove( requiredOpts.indexOf(key) );
            }
            requiredOpts.add(key);
        }

        shortOpts.put(key, opt);

        return this;
    }

    public Collection getOptions()
    {
        return Collections.unmodifiableCollection(helpOptions());
    }

    List helpOptions()
    {
        List opts = new ArrayList(shortOpts.values());

        Iterator iter = longOpts.values().iterator();

        while (iter.hasNext())
        {
            Object item = iter.next();

            if (!opts.contains(item))
            {
                opts.add(item);
            }
        }

        return new ArrayList(opts);
    }

    public List getRequiredOptions()
    {
        return requiredOpts;
    }

    public Option getOption(String opt)
    {
        opt = Util.stripLeadingHyphens(opt);

        if (shortOpts.containsKey(opt))
        {
            return (Option) shortOpts.get(opt);
        }

        return (Option) longOpts.get(opt);
    }

    public boolean hasOption(String opt)
    {
        opt = Util.stripLeadingHyphens(opt);

        return shortOpts.containsKey(opt) || longOpts.containsKey(opt);
    }

    public OptionGroup getOptionGroup(Option opt)
    {
        return (OptionGroup) optionGroups.get(opt.getKey());
    }

    public String toString()
    {
        StringBuffer buf = new StringBuffer();

        buf.append("[ Options: [ short ");
        buf.append(shortOpts.toString());
        buf.append(" ] [ long ");
        buf.append(longOpts);
        buf.append(" ]");

        return buf.toString();
    }
}