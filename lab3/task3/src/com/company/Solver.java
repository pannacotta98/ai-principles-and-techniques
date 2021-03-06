package com.company;

import java.util.*;

// Heccin Java, hows it even workz
public class Solver {
    public HashSet<Clause> KB = new HashSet<>();
    static Random rnd = new Random();

    Solver(String[] KB) {
        for (String str : KB) this.KB.add(new Clause(str));
    }

    public HashSet<Clause> solve() {
        HashSet<Clause> S = new HashSet<>();
        HashSet<Clause> KBPrime;

        do {
            S.clear();
            KBPrime = new HashSet<>(KB);

            ArrayList<Clause> tempKB = new ArrayList<>(KB);
            for (int i = 0; i < tempKB.size() - 1; i++) {
                for (int j = i + 1; j < tempKB.size(); j++) {
                    Clause C = resolution(tempKB.get(i), tempKB.get(j));
                    // If i and j can be resolved into a new clause
                    if (C != null) {
                        S.add(C);
                    }
                }

            }

            if (S.isEmpty()) return KB;

            incorporate(S, KB);
        } while (!KB.equals(KBPrime));

        return KB;
    }

    // Directly modifies KB
    public static void incorporate(HashSet<Clause> S, HashSet<Clause> KB) {
        for (Clause A : S) {
            incorporateClause(A, KB);
        }
    }

    // Directly modifies KB
    public static void incorporateClause(Clause A, HashSet<Clause> KB) {
        KB.removeIf(A::subsumesStrict);
        KB.add(A);
    }

    static public Clause resolution(Clause AIn, Clause BIn) {
        Clause A = new Clause(AIn);
        Clause B = new Clause(BIn);
        if (Collections.disjoint(A.positive, B.negative) && Collections.disjoint(A.negative, B.positive)) {
            return null;
        }

        if (!Collections.disjoint(A.positive, B.negative)) {
            String a = pickRandomFromIntersection(A.positive, B.negative);
            A.positive.remove(a);
            B.negative.remove(a);
        } else {
            String a = pickRandomFromIntersection(A.negative, B.positive);
            A.negative.remove(a);
            B.positive.remove(a);
        }

        Clause C = new Clause();
        C.positive = unionAsCopy(A.positive, B.positive);
        C.negative = unionAsCopy(A.negative, B.negative);

        // Is C a tautology?
        if (!Collections.disjoint(C.positive, C.negative)) {
            return null;
        }

        // Since C.positive and C.negative are sets there should be no duplicates
        return C;
    }

    static private HashSet<String> unionAsCopy(HashSet<String> set1, HashSet<String> set2) {
        HashSet<String> union = new HashSet<>(set1);
        union.addAll(set2);
        return union;
    }

    static private HashSet<String> intersectionAsCopy(HashSet<String> set1, HashSet<String> set2) {
        HashSet<String> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        return intersection;
    }

    static private String pickRandomFromIntersection(HashSet<String> set1, HashSet<String> set2) {
        HashSet<String> intersection = intersectionAsCopy(set1, set2);
        // Probably not super efficient but hey, it's just a lab and intersection is not that big
        String[] array = intersection.toArray(new String[0]);
        int randIdx = rnd.nextInt(array.length);
        return array[randIdx];
    }
}
