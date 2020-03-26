# MAT335COVID-19
Mathamatical modeling pertaining to covid-19


MAKE SURE TO ALWAYS BE ON YOUR OWN BRANCH

Please make your own branch with the command:
git checkout -b "name_of_branch"

To commit the branch to the repo use:
git push origin "name_of_branch"

To connect to the repository:
git push --set-upstream origin "name_of_branch"

To add all files just use:
git add -A .

To prepare files for pushing:
git commit -m "message about what your are about to commit"

To actually add them to the repo:
git push


!!!!!!!
Merging to master will be a group effort never do it on your own
!!!!!!!

Data is for the data pipeline of covid-19 cases and setting up the information therein for testing

Models is going to have all the models that we could test (Will inherit from a base class)

Runscripts is actually the code for testing an entire model

Assesment is code for verifying the accuracy of the model, includeds error calculation and viewing of data