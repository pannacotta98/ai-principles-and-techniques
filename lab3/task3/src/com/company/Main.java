package com.company;

import java.util.HashSet;

public class Main {

    public static void main(String[] args) {
//        // Test Resolution
//        Clause A = new Clause("a|b|-c");
//        Clause B = new Clause("c|b");
//        System.out.println("Resolution(" + A + ", " + B + ") = " + Solver.resolution(A, B));
//        A = new Clause("a|b|-c");
//        B = new Clause("d|b|-g");
//        System.out.println("Resolution(" + A + ", " + B + ") = " + Solver.resolution(A, B));
//        A = new Clause("-b|c|t");
//        B = new Clause("-c|z|b");
//        System.out.println("Resolution(" + A + ", " + B + ") = " + Solver.resolution(A, B));

//        // Test subsumption
//        System.out.println(new Clause("c|a").subsumesStrict(new Clause("a|b|c")) == true);
//        System.out.println(new Clause("b|-c").subsumesStrict(new Clause("a|b|-c")) == true);
//        System.out.println(new Clause("b|-f|-c").subsumesStrict(new Clause("a|b|-c")) == false);
//        System.out.println(new Clause("b").subsumesStrict(new Clause("a|b|-c")) == true);
//        System.out.println(new Clause("b|-c|a").subsumesStrict(new Clause("a|b|-c")) == false);
//        System.out.println(new Clause("b|-c|a").subsumesOrEqual(new Clause("a|b|-c")) == true);

//        // Test equals
//        Clause C = new Clause("a");
//        Clause anotherC = new Clause("a");
//        Clause D = new Clause("b|g|d");
//        Clause E = new Clause("-a");
//        Clause F = new Clause("ice|-movie|-sun");
//        Clause anotherF = new Clause("ice|-movie|-sun");
//        System.out.println(C.equals(C));
//        System.out.println(C.equals(anotherC));
//        System.out.println(C.equals(D));
//        System.out.println(C.equals(E));
//        System.out.println(F.equals(F));
//        System.out.println(F.equals(anotherF));

//        // Other testing
//        Clause mov = new Clause("movie");
////        Clause test = new Clause("ice |")
//        Clause evilOne = new Clause("movie | ice | -money");
//        System.out.println(mov.subsumesOrEqual(evilOne));
//        System.out.println(evilOne.subsumesOrEqual(mov));

        System.out.println("Task A");
        Solver agentBobSolver = new Solver(new String[]{
                "-sun | -money | ice",
                "-money | ice | movie",
                "-movie | money",
                "-movie | -ice",

                "movie"
        });
        HashSet<Clause> result = agentBobSolver.solve();
        System.out.println(result);

        System.out.println("\nTask B: Robbery puzzle");
        Solver robberySolver = new Solver(new String[]{
                "A | B | C",
                "-C | A", // C => A
                "-B | A | C" // B => (A v C)
        });
        System.out.println(robberySolver.solve());

    }
}
