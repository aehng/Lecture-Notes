#!/usr/bin/env csi
;;; The Scheme code in this file is compatible with Chicken Scheme version 5
;;;
;;; It may require tweaking to run in a different Scheme implementation.

(import
  (chicken process-context) ; command-line-arguments
  srfi-1                    ; circular-list
  srfi-18)                  ; thread-sleep!

(define *DELAY_SEC* 0.00001)

(define lyrics
  (apply circular-list (string->list
"This is the song that never ends
It just goes on and on my friends
Some people started singing it, not knowing what it was
And they'll continue singing it forever just because
")))

(define play-one-note
  (lambda (c)
    (print* c)  ; The print* function is Chicken-specific
                ; it flushes STDOUT after each write.
    (thread-sleep! *DELAY_SEC*)))

(define sing
  (lambda (song)
    (play-one-note (car song))   
    (sing (cdr song))))


(print "This is the Scheme version")

(cond
  ((zero? (length (command-line-arguments)))
   (print "Singing recursively\n")
   (thread-sleep! 1.5)
   (sing lyrics))
  (else
    (print "Singing iteratively (j/k, this actually is recursive, too!)\n")
    (thread-sleep! 1.5)
    (for-each play-one-note lyrics)))
