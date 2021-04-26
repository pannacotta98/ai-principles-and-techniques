package com.company;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Objects;

public class Clause {
    public HashSet<String> positive = new HashSet<>();
    public HashSet<String> negative = new HashSet<>();

    Clause() {}

    Clause(String arg1) {
        arg1 = arg1.replaceAll(" ", "");
        String[] literals = arg1.split("\\|");

        for (String lit : literals) {
            if (lit.contains("-")) {
                lit = lit.replace("-", "");
                negative.add(lit);
            } else {
                positive.add(lit);
            }
        }
    }

    Clause(Clause c) {
        this.positive = new HashSet<>(c.positive);
        this.negative = new HashSet<>(c.negative);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Clause clause = (Clause) o;
        return Objects.equals(positive, clause.positive) && Objects.equals(negative, clause.negative);
    }

    @Override
    public int hashCode() {
        return Objects.hash(positive, negative);
    }

    public boolean subsumesOrEqual(Clause B) {
        return B.negative.containsAll(this.negative)
                && B.positive.containsAll(this.positive);
    }

    public boolean subsumesStrict(Clause B) {
//        return this.subsumesOrEqual(B)
//                && !this.negative.equals(B.negative)
//                && !this.positive.equals(B.positive);
        return this.subsumesOrEqual(B) && !B.subsumesOrEqual(this);
    }

    @Override
    public String toString() {
        String[] signedLiterals = new String[positive.size() + negative.size()];
        int idx = 0;
        for (String lit : positive) signedLiterals[idx++] = lit;
        for (String lit : negative) signedLiterals[idx++] = "-" + lit;
        return "{ " + String.join("|", signedLiterals) + " }";
    }
}
