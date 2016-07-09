Classes
A namespace is a mapping from names to objects. Example of namespace are: the set
of built-in names(containing functions such as abs(), and built-in exception names)

An attribute  a word for any name following a dot. For example, in the expression z.real, real
is an attribute of the object z. References to names in models are attribute references.

Namespaces are created at diffrent moments and have different lifetimes. The global namespace ofr a modules i create when the
the module definition is read in. Weell it lasts until the interpreter quits.

If a namespace is declared gloabal, then all references and assignments fo directly to the middles scope
containing the modules glbal names.

When a class definition is entered, a new namespace is created ,and used as the local scope, thus, all assignments to local variables go into
this new namespaces.