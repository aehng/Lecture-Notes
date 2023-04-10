// Attached is a version of the song that never ends written for Kotlin. You'll
// probably want to grab the command-line compiler. See:
// https://kotlinlang.org/docs/command-line.html Interestingly enough, Not only
// can Kotlin compile for the JVM, but apparently it can also compile down to
// native code (at the likely cost of losing Java interoperability, but you still
// get C interop).
//
// There were quite a few things that I found interesting to note from this
// exercise that I'll mention below.
//
// I'm not going to claim being a Kotlin expert or that I necessarily followed the
// language paradigms entirely in line with the Kotlin-standard methodology, but I
// tried to be very deliberate in following their common design patterns and
// recommendations as closely as I could.
//
// The song program is quite a bit more concise in Kotlin than in java, about 20
// lines shorter if you exclude blank lines and comment lines. The Kotlin version
// has about 52 lines after         excluding comments and blank lines. This is
// just slightly more than  your python implementation when you exclude blank
// lines and comments (49), making only the Scheme version significantly  smaller
// than the Kotlin version out of all implementations you have shown me so far.
// The C versions all had more lines of code, anywhere from a little less than 10
// (C++) to about 15 (C)     more.
// p
// A lot of this is probably due to Kotlin's major reduction of boilerplate code.
// I didn't need to write a single import statement. You also don't have to
// include the throws keyword for        functions that may throw an exception.
// Kotlin also practically eliminates the need for writing the most common getters
// and setters. Additionally, your main function doesn't need to be in a  class.
// You can have top-level functions in a file. This is a nice touch and I can see
// why Kotlin also has support for being run as a scripting language as well.
// Kotlin apparently even has a REPL since it's being designed to work as both a
// compiled and scripted language.
//
// Perhaps the most interesting part of this exercise was also discovering how
// Kotlin is designed to be very null-safe. NullPointerExceptions are meant to be
// uncommon and every class member    must be initialized with a default value.
// Null is only an option for initialization if you append ? to the end of the
// type to specify nullability. Kotlin generally treats nullable and
// non-nullable variables as different types, requiring an explicit non-null
// assertion to take a nullable value and assign it to a non-nullable value.
// There's actually a good example of when   you would want to do this in the
// Circular List implementation. The implementation of CircularList will look a
// bit different because of Kotlin's initialization requirements/paradigms. It
// certainly enforces a more null-safe approach to how one would even structure
// the code.
//
// Out of curiosity, I decompiled the class file that kotlin produces for the Java
// Runtime and the recursive and iterative versions ended up looking almost
// exactly identical. I am curious to   see how the assembly would look if I
// compiled this down to native code since Kotlin uses LLVM for native
// compilation. I suspect that the final output will either look similar to what
// clang  spits out, or it would look like a standard loop inside the function.
// From what I've seen from C compilers when they do tail call optimization, they
// jump to the function routine's start     without updating the return address
// pointer instead of doing a traditional call, which modifies the return address
// pointer.
//
// A few other interesting aspects of Kotlin are that it *actually* makes
// everything an object (internally using primitives on compile if possible for
// performance), kind of like how Ruby does  that, while also having syntax that
// is reminiscent of TypeScript. Additionally, it supports receiver-style
// functions, similar to what you may see in Go with an additional coroutines
// feature that seems to be very Go-inspired. It's also got some nice syntax
// additions.
//
// Hope you find this as interesting as I did!
//
// - Kyler




const val DELAY_MS: Long = 1
const val LYRICS: String =
"""This is the song that never ends
It just goes on and on my friends
Some people started singing it, not knowing what it was
And they'll continue singing it forever just because
"""

class Letter(val c: Char) {
    var next: Letter? = null
}

// This is the largest deviation from the Java version. Because of Kotlin's null-safety features
// and the programming style that comes along with that.
class CircularList(letters: String) {

    private var head: Letter = Letter(letters[0])
    val char get() = this.head.c

    init {
        var f: Letter = head

        for (c: Char in letters.slice(1 until letters.length)) {
            val next  = Letter(c)
            f.next = next
            f = next
        }

        f.next = head
    }

    fun next(): CircularList {
        // If next is ever null at this point, the programmer has failed to set up the circular list properly.
        // This is an appropriate point to assert non-null, causing a NullPointerException if it is null.
        // Kotlin is designed with a lot of built-in null-safety
        this.head = this.head.next!!
        return this
    }
}

fun main(args: Array<String>) {
    println("This is the Kotlin version")
    val song = CircularList(LYRICS)

    if (args.isEmpty()) {
        println("Singing recursively\n")
        Thread.sleep(1500)
        recursive(song)
    } else {
        println("Singing iteratively\n")
        Thread.sleep(1500)
        iterative(song)
    }
}

fun iterative(cl: CircularList) {
    while (true) {
        print(cl.char)
        cl.next()
        Thread.sleep(DELAY_MS)
    }
}

// To make a function tail call optimized, Kotlin requires explicitly
// specifying it in the function declaration.
tailrec fun recursive(cl: CircularList) {
    Thread.sleep(DELAY_MS)
    print(cl.char)
    recursive(cl.next())
}
