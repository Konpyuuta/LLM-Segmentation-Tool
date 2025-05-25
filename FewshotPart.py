'''

@author Maurice Amon
'''

fewshot_part = '''SOURCE-CODE: 

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

Prompt: Take a look at the java-code under SOURCE-CODE above and build semantically coherent code-fragments by dividing the code with ### as a delimiter. Only give the code-fragments as a response, omit everything else.
Answer: 

###
import java.util.*;
###

###
public class TfIdf {
###

###
    private Integer alpha;
##

###
    public static double tf(List<String> doc, String term) {
###

###
        int termCount = 0;
###

###
        int totalTerms = doc.size();
###

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
    
###
    public static double idf(List<List<String>> docs, String term) {
###
        int totalDocs = docs.size();
###

###
        int docsWithTerm = 0;
###

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

###
        double idf = Math.log((double) totalDocs / (1 + docsWithTerm));
        return idf;
###

###
    public static double tfidf(List<String> doc, List<List<String>> docs, String term) {
###

###
        double tf = tf(doc, term);
        double idf = idf(docs, term);
        return tf * idf;
###

Prompt: Take a look at the java-code under SOURCE-CODE below and build semantically coherent code-fragments by dividing the code with ### as a delimiter. Only give the code-fragments as a response, omit everything else.
'''