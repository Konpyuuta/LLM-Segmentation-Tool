

real_meta_part = '''
**Prompt:**

---

**Task:**

Split the given source code under SOURCE-CODE into syntactically and semantically coherent fragments by inserting `###` as a delimiter. The goal is to produce code fragments that are meaningful, self-contained, and small enough to be used for Delta Debugging analysis.

**Guidelines:**

* Each fragment must be no longer than 5 lines.

* Each fragment should represent a logical code unit, such as:

  * a package or import statement
  * a class or interface declaration
  * a method signature (with its parameter list)
  * a block of related statements (e.g., variable declarations, loops, conditionals)

* **Large methods must be split** into smaller, logical sections. For example:

  * Variable declarations
  * Loops
  * Conditional blocks
  * Return statements

* **However, do not split apart directly dependent statements.** For example:

  * If a variable is declared and immediately used in the next statement(s), keep those together.
  * For example, in a block like:

    ###
    Collection processed = options.values();
    Option[] optionsArray = new Option[processed.size()];
    return (Option[]) processed.toArray(optionsArray);
    ###

    These lines are **dependent** and must remain as a single fragment.

* Avoid splitting inside a single statement or expression.

* Fragments should remain syntactically correct and semantically clear.

* The prompt should work for Java and similar languages.

---

**Example Input:**

```java
import java.util.*;

public class TfIdf {

    private Integer alpha;

    public static double tf(List<String> doc, String term) {
        int termCount = 0;
        int totalTerms = doc.size();
        for (String word : doc) {
            if (word.equalsIgnoreCase(term)) {
                termCount++;
            }
        }
        double tf = (double) termCount / totalTerms;
        return tf;
    }
    
    public static double idf(List<List<String>> docs, String term) {
        int totalDocs = docs.size();
        int docsWithTerm = 0;
        for (List<String> document : docs) {
            for (String word : document) {
                if (word.equalsIgnoreCase(term)) {
                    docsWithTerm++;
                    break;
                }
            }
        }     
        double idf = Math.log((double) totalDocs / (1 + docsWithTerm));
        return idf;
    }

    public static double tfidf(List<String> doc, List<List<String>> docs, String term) {
        double tf = tf(doc, term);
        double idf = idf(docs, term);
        return tf * idf;
    }
}
```

---

**Expected Output:**

```java
import java.util.*;
###
public class TfIdf {
###
    private Integer alpha;
###
    public static double tf(List<String> doc, String term) {
###
        int termCount = 0;
###
        int totalTerms = doc.size();
###
        for (String word : doc) {
            if (word.equalsIgnoreCase(term)) {
                termCount++;
            }
        }
###
        double tf = (double) termCount / totalTerms;
        return tf;
###
    }
###
    public static double idf(List<List<String>> docs, String term) {
###
        int totalDocs = docs.size();
###
        int docsWithTerm = 0;
###
        for (List<String> document : docs) {
            for (String word : document) {
                if (word.equalsIgnoreCase(term)) {
                    docsWithTerm++;
                    break;
                }
            }
        }
###
        double idf = Math.log((double) totalDocs / (1 + docsWithTerm));
        return idf;
###
    public static double tfidf(List<String> doc, List<List<String>> docs, String term) {
###
        double tf = tf(doc, term);
        double idf = idf(docs, term);
        return tf * idf;
###
    }
###

'''

