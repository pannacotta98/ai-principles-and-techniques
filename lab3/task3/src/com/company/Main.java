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

        Solver agentBobSolver = new Solver(new String[]{
                "-sun | -money | ice",
                "-money | ice | movie",
                "-movie | money",
                "-movie | -ice",

                "movie"
        });

        HashSet<Clause> result = agentBobSolver.solve();
        System.out.println(result);

    }
}
