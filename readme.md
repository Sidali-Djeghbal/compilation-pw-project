# MiniPascal-FR Compiler Project

## Overview
This project involves the design and implementation of a compiler for the MiniPascal-FR programming language. The compiler will consist of two main components:
1. **Scanner (Scanner2025):** Responsible for lexical analysis.
2. **Parser (Parser2025):** Responsible for syntactic analysis.

---

## Grammar of MiniPascal-FR
The grammar of the MiniPascal-FR language is defined in Backus-Naur Form (BNF):

### Program Structure
```
<ProgrammePascal> ::= programme <NomProgramme> ; <Corps> .
<Corps> ::= [<PartieDéfinitionConstante>] [<PartieDéfinitionVariable>] <InstrComp>
```

### Constants and Variables
```
<PartieDéfinitionConstante> ::= constante <DéfinitionConstante> {<DéfinitionConstante>}
<DéfinitionConstante> ::= <NomConstante> = <Constante> ;
<PartieDéfinitionVariable> ::= variable <DéfinitionVariable> {<DéfinitionVariable>}
<DéfinitionVariable> ::= <GroupeVariable> ;
<GroupeVariable> ::= <NomVariable> {, <NomVariable>} : <NomType>
<NomVariable> ::= <Nom>
<Nom> ::= <Lettre> <Chiffre> {<Lettre> / <Chiffre>}
<Lettre> ::= 'A' / 'B' / ... / 'Z' / 'a' / ... / 'z'
<Chiffre> ::= 0 / 1 / ... / 9
<NomType> ::= entier / reel
<NomConstante> ::= <Nom>
<Constante> ::= <Nombre> / <NomConstante>
<NomProgramme> ::= <Nom>
<Nombre> ::= <Chiffre> {<Chiffre>} / <Chiffre><Chiffre> {<Chiffre>} .<Chiffre>{<Chiffre>}
```

### Instructions
```
<InstrComp> ::= debut <Instruction> {; <Instruction>} fin
<Instruction> ::= <InstructionAffectation> / <InstructionSi> / <InstructionTantque> /
                   <InstructionRépéter> / <InstrComp> / <InstructionPour> / <Vide>
<InstructionAffectation> ::= <NomVariable> := <Expression>
<Expression> ::= <ExpressionSimple> [<OperateurRelationnel> <ExpressionSimple>]
<OperateurRelationnel> ::= < / > / = / <= / >= / <>
<ExpressionSimple> ::= [<OperateurSigne>] <Terme> {<OperateurAddition> <Terme>}
<OperateurSigne> ::= + / -
<OperateurAddition> ::= + / - / ou
<Terme> ::= <Facteur> {<OperateurMult> <Facteur>}
<OperateurMult> ::= * / div / mod / et
<Facteur> ::= <Constante> / <NomVariable> / (<Expression>)
<InstructionSi> ::= si <Expression> alors <Instruction> [sinon <Instruction>]
<InstructionTantque> ::= tantque <Expression> faire <Instruction>
<InstructionRépéter> ::= repeter <Instruction> jusqu’a <Expression>
<InstructionPour> ::= pour <NomVariable> allant de <Constante> a <Constante> [pas <Constante>] faire <Instruction>
<Vide> ::= ''
```

---

## Deadlines
- **Scanner2025 Validation:** December 1, 2025
- **Parser2025 Validation:** January 12, 2026

---

## Additional Notes
- The responsible teacher will validate the students' programs. Students must follow the teacher's instructions.
- Students can work in pairs but not in groups of three.

---

## How to Run
- run `main.py` (no 3rd party libraries needed).

---

## TO-DO 
1. **Scanner Implementation:**
   - [ ] Design and implement a scanner for the MiniPascal-FR language.
   - [ ] Store the output in a file named `TOKEN`.
   - [ ] Display the sequence of tokens, the symbol table, and any errors with their types on the screen.

3. **Parser Implementation:**
   - [ ] Design and implement a recursive descent parser for the MiniPascal-FR language.
   - [ ] Store the output in a file named `RULE`.
   - [ ] Display the sequence of rules corresponding to the source program and any errors with their types on the screen.
