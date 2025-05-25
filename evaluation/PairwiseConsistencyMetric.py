'''

@author Maurice Amon
'''
from itertools import combinations

from sklearn.metrics import precision_score, recall_score, f1_score


class PairwiseConsistencyMetric:

    _precision = None

    _recall = None

    _f1_score = None

    _ideal_boundaries = None

    _predicted_boundaries = None

    _lines = None

    def __init__(self, ideal_boundaries, predicted_boundaries, lines):
        self._ideal_boundaries = ideal_boundaries
        self._predicted_boundaries = predicted_boundaries
        self._lines = lines

    def segmentation_to_labels(self, lines, boundaries):

        labels = [0] * lines
        segment_id = 0
        last = 0
        for boundary in boundaries:
            for i in range(last, boundary + 1):
                labels[i] = segment_id
            last = boundary + 1
            segment_id += 1
        for i in range(last, lines):
            labels[i] = segment_id
        return labels

    def pairwise_consistency_metric(self):
        ideal_labels = self.segmentation_to_labels(self._ideal_boundaries, self._lines)
        predicted_labels = self.segmentation_to_labels(self._predicted_boundaries, self._lines)

        true_pairs = []
        pred_pairs = []

        for i, j in combinations(range(self._lines), 2):
            same_ref = int(ideal_labels[i] == ideal_labels[j])
            same_pred = int(predicted_labels[i] == predicted_labels[j])
            true_pairs.append(same_ref)
            pred_pairs.append(same_pred)

        self._precision = precision_score(true_pairs, pred_pairs)
        self._recall = recall_score(true_pairs, pred_pairs)
        self._f1_score = f1_score(true_pairs, pred_pairs)
        return self._precision, self._recall, self._f1_score

    def test(self):
        # Example source code (each string is a line)
        code_lines = [
            "def add(a, b):",
            "    return a + b",
            "",
            "def multiply(x, y):",
            "    return x * y",
            "",
            "print(add(2, 3))",
            "print(multiply(4, 5))"
        ]

        total_lines = len(code_lines)

        # Reference segmentation (manually labeled)
        reference_boundaries = [1, 4, 5]  # Lines 0–1, 2–4, 5–...

        # Predicted segmentation (from your tool/heuristic)
        predicted_boundaries = [1, 3, 6]

        # Evaluate
        precision, recall, f1 = self.pairwise_consistency_metric(reference_boundaries, predicted_boundaries, total_lines)
        print(f"Pairwise Precision: {precision:.2f}")
        print(f"Pairwise Recall:    {recall:.2f}")
        print(f"Pairwise F1 Score:  {f1:.2f}")
