# Advanced Git

* [A review of Git basics](#a-review-of-git-basics)
* [Experimentation with branches](#experimentation-with-branches)
* [Resolving merge conflicts](#resolving-merge-conflicts)
* [Throwing away bad work: a word of warning](#throwing-away-bad-work-a-word-of-warning)
* [Get rid of *uncommitted* changes with `git checkout` or `git restore`](#get-rid-of-uncommitted-changes-with-git-checkout-or-git-restore)
* [Get rid of *committed but un-pushed* changes with `git reset --hard`](#get-rid-of-committed-but-un-pushed-changes-with-git-reset-hard)
* [Get rid of *committed* and *pushed* changes with `git revert`](#get-rid-of-committed-and-pushed-changes-with-git-revert)
* [Which idiot is to blame for this awful code?](#which-idiot-is-to-blame-for-this-awful-code)
* [Using `git bisect` to track down a bug](#using-git-bisect-to-track-down-a-bug)


## A review of Git basics

    $ git help ...
    $ git glossary
    $ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn3.git
    $ git remote rename origin old-origin
    $ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn3.git
    $ nano src/Bingo.py
    $ git diff
    $ git stash
    $ git stash pop
    $ git add FILENAME ...
    $ git commit -m "Commit Message"
    $ git tag designed
    $ git log
    $ git push origin master designed

### How to refer to objects in Git

A Git **object** may be referred to by any of these names:

0.  An SHA-1 commit name, a.k.a. the "true name" (e.g.
    `6b0fdef75fc709f95aedda60b9693093e086710e` or an abbreviation `6b0fdef7`)
1.  `HEAD`, referring to the currently checked-out commit.  This is the Git
    equivalent to the current working directory `.` in the terminal.
2.  A name of a branch (i.e. `master`, `origin/master`)
3.  The name of a tag
4.  A revision that is `N` generations older than a named commit.  Combine the
    name of the base commit with a generation number using a tilde `~`.  For
    example:
    *    `HEAD~1` is the previous commit
    *    `master~3` is the great-grandparent commit of the tip of the branch `master`
    *    `deployed~2` is the 2nd-to-last commit before you finished the *deployment* phase of an assignment

Read `git help revisions` to learn all of the ways you can refer to commit
objects in the log.



## Experimentation with branches

One of Git's biggest selling-points over other version control systems is its
branching system.  Branches in Git are easy to *make*, easy to *delete*, and
easy to *merge*.  They are an excellent way for you to confidently experiment
with your code.

With branches your workflow may go like this:

0.  Dive in and start making a risky change.
1.  At any time before you commit, you can decide to create a new branch.
2.  Now your commits cause the new branch to grow, instead of the master branch.
3.  If your experiment fails, you can easily return to the master branch.
4.  If your experiment succeeds, you can merge the new branch into master.

The images in this tutorial by Atlassian may help you visualize what's going on
with branches:

https://www.atlassian.com/git/tutorials/using-branches


### `git checkout -b BRANCHNAME`
### `git switch -c BRANCHNAME`
Create a new branch named `BRANCHNAME`, and make it the current branch.  `HEAD`
still points to the same commit that you were on before, but *new* commits will
now be added to this branch.  New commits will not become a part of the old
branch you were on.

*`git switch` was added in version 2.23 (August 2019).  In the unlikely event you get an error message when using that command, consider updating to a newer version of Git*


### `git checkout BRANCHNAME`
### `git switch BRANCHNAME`
Make the branch `BRANCHNAME` become the current branch.

This involves editing the currently checked-out files (the working tree) to match their configuration in the target branch.  If doing so would cause your uncommitted changes to be lost, Git will stop and ask you to take action (either to commit or stash your changes).


### `git branch`
List the branches you have checked out in this repo.


### `git branch -a`
List all of the branches in your repo, including branches from the remote
repositories you have fetched from.


### `git show-branch`
List all of the branches you have checked out in this repo, and show which
commits belong to each one. Branches contain the same commit when the `*` or
`+` symbols are present in each of their columns.


### `git show-branch --more=10`
Git's show-branch command stops displaying history as soon as it reaches the
earliest common ancestor for all commits. The --more argument tells it to go
back further, if possible.


### `git log --graph`
Draw an ASCII-art family tree of commits, nicely illustrating how merges have
worked out through history.

Ordinarily, Git commits have exactly *one* parent.  Merges result from one
commit having two or more parents.


### `git branch -d BRANCHNAME`
Safely delete the branch `BRANCHNAME`.

Git will not allow you to delete a branch whose commits are not also present in
another branch.  Use `git branch -d` after you have successfully merged one of
your experimental branches into a permanent branch such as `master`.


### `git branch -D BRANCHNAME`
Dangerously delete the branch `BRANCHNAME`.

Use  `git branch -D` when you have determined that your experiment has gone
terribly wrong, and you're positive that you will never need to even look at
this code ever again.

It should be noted that the commits don't actually go anywhere; the name of the
branch is the only thing which is truly deleted. But without a name it is
difficult for you to recover those lost commits. This is why deleting branches
should only be done with care.


### `git push REMOTE BRANCHNAME`
Send commits in `BRANCHNAME` to `REMOTE`.

So far you've only been pushing your master branch to GitLab.  You can push
other branches, too.  The GitLab website defaults to showing the master branch,
but you can view commits in other branches as well.

Because we see the master branch by default, this is the branch that will be
graded.  Make sure that your master branch contains all commits that make up
your final submission.


### `git merge BRANCHNAME`
Make the commits in `BRANCHNAME` become part of the currently checked-out branch.

If you are following best-practices and keeping all risky work off the master
branch, there will come a time when you decide that your experiment is a
success that deserves to be publicized.  The `merge` command is how to conclude
a successful experiment.

Generally, you will first run `git checkout master` or a similar command before
merging your work into permanent branch.

    $ git checkout experiment
    $ vim main.py
    ...
    $ git add main.py
    $ git commit -m Eureka\!\!\!
    $ git checkout master
    $ git merge experiment




## Resolving merge conflicts

When merging two branches into one there is a risk that a conflict will occur.
When you use the merge command you are asking Git to combine multiple versions
of a file into one.

#### Merge conflict

A *merge conflict* occurs when two or more commits merged from different
branches change the same portion of the same file.  Git cannot automatically
proceed merge without losing data and halts the merge.  You must then review
the conflicting changes and manually bring about a resolution.

Git will annotate the affected files with *merge markers*.  These boundaries
surround the code that it appears in your branch and in the branch that is
being merged in.

Clone my [merge-conflict](https://gitlab.cs.usu.edu/erik.falor/merge-conflict) repo from GitLab and follow along with me.


```
$ git clone git@gitlab.cs.usu.edu:erik.falor/merge-conflict.git

$ cd merge-conflict

$ git merge fib
Updating ffa9653..5b1b969
Fast-forward
 hello.py | 9 ++++++++-
 1 file changed, 8 insertions(+), 1 deletion(-)

$ git merge fac
Auto-merging hello.py
CONFLICT (content): Merge conflict in hello.py
Automatic merge failed; fix conflicts and then commit the result.
```

At this point you, the human, must step in and fix `hello.py`.  Locate the
conflicting *hunks* in the file and rewrite them so that the new program makes
sense.

Hunks are denoted by *conflict markers* `<<<<<<<`, `=======`, and `>>>>>>>` .

```python
<<<<<<< HEAD
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def hello(who, n):
    for i in range(fib(n)):
=======
def fac(n):
    if n < 2:
        return 1
    else:
        return n * fac(n-1)


def hello(who, n):
    for i in range(fac(n)):
>>>>>>> fac
        print(f"{i:3}: Hello {who}")


# Is it lunch time yet?
hello('Fries!!', 4)
hello('Hamburgers!!', 5)
```


The first hunk between `<<<<<<<` and `=======` denotes the code in
your currently-checked out commit (that's what `HEAD` means, after all).

Code between `=======` and `>>>>>>>` came from a branch named `fac`.

Do you see the conflict?  There are two different versions of the `hello()`
function, one which calls `fib()`, and the other calling `fac()` on the same
line.  We can't have both at the same time, and so Git has halted the merge.
It takes a human to decide how to untie this knot.

One way to resolve the conflict is to create two functions:

```python
def helloFib(who, n):
    for i in range(fib(n)):
        print(f"Hello {who}")

def helloFactorial(who, n):
    for i in range(fac(n)):
        print(f"Hello {who}")
```


Then I'd have to visit every place in the program where `hello()` had been used
and change those calls to use one of the above functions.

Alternatively, I could stick with one version of `hello()` but change the
number of parameters it takes.  In this version I pass either the `fib` or
the `fac()` function as a parameter:

```python
def hello(who, fn, n):
    for i in range(fn(n)):
        print(f"Hello {who}")

# Is it lunch time yet?
hello('Fries!!', fib, 10)
hello('Hamburgers!!', fac, 10)
```


I still need to edit other lines of code by adding a new argument to each call
to the function `hello()`.  Whatever my choice, it will be much more
sophisticated than what Git can come up with.  Once I have changed the code and
removed the conflict markers, I run `git add` followed by `git commit` to
conclude the merge.


### I don't do conflict, I give up!

If you can't (or don't want to) deal with the conflicting code right now
you can undo the merge with `git merge --abort`:

	$ git status
	On branch master
	You have unmerged paths.
	  (fix conflicts and run "git commit")
	  (use "git merge --abort" to abort the merge)

	Unmerged paths:
	  (use "git add <file>..." to mark resolution)
		both modified:   hello.py

	no changes added to commit (use "git add" and/or "git commit -a")


	$ git merge --abort

	$ git status
	On branch master
	nothing to commit, working tree clean



## Throwing away bad work: a word of warning

In the next section I will teach you how to use some commands which, used
unwisely, can result in a broken repository.  As Git has a mind like a steel
trap it's actually quite hard to make Git forget things entirely.  The trick
lies in cajoling Git into remembering.

### `git reflog`
You ought to pay close attention any time Git shows a message containing a
SHA-1 sum; Git will do that whenever it thinks you're about to do something
risky.  

But sometimes mistakes happen.  This powerful command displays the log of
repository-modifying actions that Git has undertaken *in your local
repository*.

This information *may* be used to track down commits which have been pruned off
of the tree.  But there are caveats.

0.  The reflog only records information about `checkout` and `switch` commands taken *in your local repo* on your own computer.
1.  The reflog isn't backed up anywhere.  Notably, running `git push` does **not** sync it to the remote server.
2.  Reflog entries have an expiration date.  Exactly when they will expire is hard to say; it could be weeks or months into the future.
    *   You can manually clean the reflog by running `git gc` (garbage collect) or `git reflog expire`.
    *   In any event, there can not be any reflog entries for events before the repo was cloned.


## Get rid of *uncommitted* changes with `git checkout` or `git restore`

Sometimes you find out pretty quickly that you're barking up the wrong tree.
Or, perhaps you have accidentally deleted an important file.  Whoops!  With
Git, this is not a big deal.


### `git restore FILENAME`
### `git checkout -- FILENAME`
*   Discard changes in working directory.  This command lets you undo
    uncommitted changes on a file-by-file basis.

### `git restore .`
### `git checkout -f`
*   The nuclear option.  Discard *all* changes in the working directory,
    permanently undoing any changes which have not been committed.
*   The only way I know of to reverse the effect of this command is this unreliable procedure:
    1.  *If* your editor was running and had the affected file(s) open
    2.  *And* your editor doesn't _automagically_ re-read files from the disk when Git updates them
    3.  *Then* re-save the file from the editor's memory back to disk


### `git restore :/`
*   If the last command was the nuclear option, this is the *Tsar Bomba*
*   Undo all uncommitted changes *anywhere in the entire repository*


## Get rid of *committed but un-pushed* changes with `git reset --hard`

Other times you realize that you have not only made a mistake, but have
committed to it by permanently recording it in your repository.  Well, perhaps
"permanent" is too strong a word... if you haven't yet pushed your latest
changes to a remote repository you can erase these commits and make this appear
like nothing happened at all.  As they say, what happens in Vegas, stays in
Vegas.


### `git reset --hard REVISION`
*   Move `HEAD` and the current branch to the commit specified by REVISION.
*   If you want to undo the most recent commit, run `git reset --hard HEAD~1` where `HEAD~1` refers to the *parent* of `HEAD`.
*   You can advance both `HEAD` and the current branch forward in time, too;
    you'll just need a way to refer to that commit, perhaps by consulting `git
    reflog` or `git log`.


## Get rid of *committed* and *pushed* changes with `git revert`

The problem of playing with the timeline is that you may create a paradox or
inadvertently write yourself out of history.  The latter is possible through
using commands such as `git reset --hard` which have the power to change
commits in the past.  The negative effects will be noticed when you next try to
push your changes to a remote repository, which will notice that you are
missing a few things and refuse to accept your changes until your version of
history agrees with its own.

You can avoid this situation by *adding* instead of removing commits.  Create
and record a new commit which is the *inverse* of the commit which you wish to
remove.  This is called *reverting* a commit.  Instead of your mistake never
appearing in the log, the timeline will record the mistake and another commit
which negates it.  I don't have a tourism slogan to describe this circumstance,
I guess you'll just have to swallow your pride and own up to the fact that you
goofed up.

### `git revert -n REVISION`
*   Create and add to the staging area a commit which is the *inverse* of
    `REVISION`.
    *   Lines which were added `+` by this commit become deletions `-`, and
        vice versa.
*   By default `git revert` also does a `git commit` automatically, which puts
    you into a text editor to get your commit message about the revert.
    *   if Git thinks that you like to use Vim, you may have a bad time.
    *   The `-n` switch avoids automatically committing the change, and thus
        avoids dumping you into Vim


## Which idiot is to blame for this awful code?

This is question that will cross your mind from time to time.  You can easily
find out with the `git blame` command.

### `git blame -- FILENAME`
Annotate each line of the current version of `FILENAME` with the date &
committer who last changed it.  I hope it wasn't you!  Keep in mind that your
psychopathic co-worker knows this command, too.

*Demo* `pushd ~/build/chicken-core.git/; git blame runtime.c`



## Using `git bisect` to track down a bug

Git's commit history of your code is an invaluable resource to help
understand the evolution of your project. However, it can become an
unmanageable resource due to its size.

Git's Bisect command is a power tool which tames the unmanageable size of your
repository.  Use it to perform a binary search on your git repo to identify the
commit which introduced a bug.

We can use `git bisect` in Vim's GitHub repository to find when a particular
bug was introduced.

[Vim no longer de-indents shell script code: Issue #2151](https://github.com/vim/vim/issues/2151#issuecomment-331970759)


### Let's track this bug down for ourselves

You can try this out for yourself on a Unix-like system with the GNU C compiler.

    $ git clone https://github.com/vim/vim.git
    $ cd vim
    $ ./configure --with-features=normal --disable-gui
    $ make -j$(nproc)


Launch the freshly-built Vim program `src/vim`:

    $ src/vim -N -u NONE -i NONE -c 'source runtime/indent/sh.vim'


If I type this text into Vim, the editor will auto-indent this shell script source code:

```sh
if this
then
    that
fi
```

In the latest version of Vim this bug is fixed, so what we see is the correct
behavior.


Let's go back in time to when the bug was occurring to see what the problem
looked like.  I'll write a shell function to make the process of re-building
and re-launching vim more convenient:

    $ function rebuild() { ./configure --with-features=normal --disable-gui; make -j$(nproc) && src/vim -Nu NONE -i NONE -c'so runtime/indent/sh.vim' }

    $ git checkout v8.0.1127
	$ rebuild


As I write that sample shell script code we will see the problem:

```sh
if this
    then
            that
            fi
```


The question is *when* did this bug occur?

From the bug report, we read that Gary noticed the problem once he built
8.0.1127, and that it wasn't there in version 8.0.0691.  Somewhere between those
two commits the bug crept into the source code.

Let's do some quick math:  `1127 - 691 = 436` commits to look at.  It won't
take too long to try each commit one-by-one until we find the one which
introduced the bug, right?

*LOL, no*.  Remember, great programmers are both lazy and impatient.  We'll
find a better way to do this.


### The Git Bisect HOWTO

You need three things to use `git bisect`:

0. The name of a commit in which the code worked
1. The name of a commit where the bug is evident
2. A test to determine the presence of the bug


To begin a bisect, checkout one of the boundary commits and run this command:

	$ git bisect start


Tell Git whether this commit is a good one or a bad one.  Because I just
demonstrated the error to you, we are on one of the **bad** commits.

	$ git bisect bad


We want to search backwards in time to find where the bug was first introduced.
So we next tell Git which commit represents the **good** boundary.  According
to the bug report we know that as of commit `v8.0.0691` Vim worked correctly.
This is the last commit which we know does not possess this bug:

	$ git bisect good v8.0.0691


Git will then take me to the commit right between our **good** and **bad**
boundaries.  There we can do whatever it takes to determine the presence of the
bug.  In this case that means re-building Vim, running it and typing some text
to see whether Vim automatically indents our code.

When we observe the absence or presence of the bug, we tell Git whether this
commit was *good* or *bad* by running either

	$ git bisect good


or

	$ git bisect bad


and re-running our test.  This process is repeated until Git converges on the
commit which introduced the bug.  In this case, we will need to repeat this
process only *8* times, way less than the 436 tests we had calculated!

But still, doing the same thing *8* times feels a little tedious.  We can
automate this process by writing a script that distinguishes between working
and broken code and telling Git to run that.  Based on the result of running
the script, Git can mark each commit as 'good' or 'bad' on its own, and proceed
to the end.

Assuming I have a program called
[`indent_bug_test.sh`](./assets/indent_bug_test.sh) which can rebuild the
program from source and detect the bug, the next command will do *all of the
work* for me:

    $ git bisect run ./indent_bug_test.sh


Once Git has converged on the broken commit we can explore the changes it
introduced to find the error behind the failure.

After we're all done, running

    $ git bisect reset


tells Git to restore the code to the way it was when we began with `git bisect
start`.


### Why this is awesome

Obviously, it's awesome because we were able to cover 436 commits in only 8
steps.  `git bisect` is an example of a binary search algorithm.  When applied
to debugging this is also known as the "Wolf Fence" debugging technique.

This technique works best when you create many small, focused commits.  We can
ask the question "would it be easier to locate this bug if there were 1/10th as
many commits which were 10x larger?"

The key to remember is that the hard part isn't locating the bad commit.
The key is that when we arrive at the bad commit our job's only just begun.

The difference between 436 commits and 43 commits isn't that great when we
apply a binary search.  We can cover 436 commits in about 8 steps, and 43
commits in 5 steps.

If the commit which introduced the bug is small and focused on a single
feature, it won't take too much work to figure out what went wrong.  Now
imagine that this commit involves 10x as many changes as before.  How long
will it take you to evaluate 120 lines of code instead of 12 lines of code?


### TL;DR

It is my advice that you make many small commits instead of a few big ones.


*Updated Mon Mar 13 15:55:17 MDT 2023*
