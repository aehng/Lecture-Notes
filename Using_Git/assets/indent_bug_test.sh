#!/usr/bin/bash

# A demonstration of `git bisect run`.
#
# This script is used by git-bisect(1) to detect the presence of a bug which
# causeed Vim's auto-indent feature to fail in Shell script files:
#   Vim no longer de-indents shell script code: Issue #2151
#   https://github.com/vim/vim/issues/2151#issuecomment-331970759

# 0. Rebuild Vim
./configure --with-features=normal --disable-gui
make -j$(nproc)


# 1. Create sample.txt by mocking up interactive input to trigger the auto-indent feature
src/vim -Nu NONE -i NONE -c 'so runtime/indent/sh.vim' -c 'normal iif thisthenthatfi' -c ':x! sample.txt'


# 2. Compare the file Vim wrote with a correct specimen,
#    saving the exit code $? into $RESULT
cmp sample.txt - <<SPECIMEN
if this
then
	that
fi
SPECIMEN
RESULT=$?


# 3. Clean up after ourselves.  This disposition of this command clobbers the
#    value in $?, which is why we copied it into $RESULT
rm -f sample.txt


# 4. Tell `git bisect` whether this commit is 'good' or 'bad' by the exit code:
# | EXIT CODE      | MEANING
# |----------------|------------------------------
# | 0              | This is a good commit
# | 1-125, 126-127 | This is a bad commit
# | 125            | Skip this commit (i.e. this code cannot be tested)
# | 128-255        | Abort git-bisect(1)
exit $RESULT
