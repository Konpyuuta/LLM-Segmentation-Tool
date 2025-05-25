'''

@author Maurice Amon
'''

cot_part = '''

Let’s go through the code line by line, deciding how to split it into small, logically coherent fragments of at most 5 lines.
Method signatures are can only be alone in a fragment.
Directly dependent lines (such as variable declarations and immediate usage) must stay together in the same fragment.

---

**Input:**

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

**Step-by-step reasoning:**

The first line ### import java.util.*; ### is a standard import statement and belongs in a separate fragment.

The next line ### public class TfIdf { ### is a class declaration, so it forms its own fragment.

The line ### private Integer alpha; ### is a field declaration and forms its own fragment.

The method signature ### public static double tf(List<String> doc, String term) { ###, will build it's own fragment.

The line ### int termCount = 0; ### is a variable declaration and forms its own fragment, as 

The line ### int totalTerms = doc.size(); ### is another variable declaration and forms its own fragment.

The for-loop:

###
for (String word : doc) {
    if (word.equalsIgnoreCase(term)) {
        termCount++;
    }
}
###

is a cohesive 5-line block and stays together as a single fragment.

The calculation and return:

###
double tf = (double) termCount / totalTerms;
return tf;
###

are directly related and small enough to remain in a single fragment.

Skip the method signature `public static double idf(List<List<String>> docs, String term) {`.

The line `int totalDocs = docs.size();` is a variable declaration and forms its own fragment.

The line `int docsWithTerm = 0;` is another variable declaration and forms its own fragment.

The nested for-loops:

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

form a cohesive block and stay together as a single fragment.

The calculation and return:

###
double idf = Math.log((double) totalDocs / (1 + docsWithTerm));
return idf;
###

are logically dependent and remain in a single fragment.

Skip the method signature `public static double tfidf(List<String> doc, List<List<String>> docs, String term) {`.

The three lines inside the last method:

###
double tf = tf(doc, term);
double idf = idf(docs, term);
return tf * idf;
###

are directly related and stay together in a single fragment.

Follow the same reasoning steps as in the example above, to build fragments of the following SOURCE-CODE: 

'''