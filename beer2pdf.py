#!/usr/bin/env python
import jinja2, pybeerxml
import tempfile, subprocess, argparse

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("inputfile", help="The beerXML file to use as input")
    argparser.add_argument("outputfile", help="The pdf file to write to")
    argparser.add_argument("-t", "--template", required=True, help="The jinja2 template to use")
    argparser.add_argument("--boiltime", type=int, help="Override boil-time with this")
    args = argparser.parse_args()

    parser = pybeerxml.Parser()
    recipes = parser.parse(args.inputfile)

    for recipe in recipes:
        if args.boiltime:
            recipe.boil_time = args.boiltime
        notes = []
        if recipe.notes:
            for noteline in recipe.notes.split('\n'):
                notes.append(noteline.strip())
        template = jinja2.Template(open(args.template,'r').read())
        output = template.render(recipe=recipe, notes=notes)

    of = tempfile.NamedTemporaryFile(mode='w')
    of.write(output)

    print("Running Inkscape ...")
    print(subprocess.check_output(['inkscape',
                               '-z',
                               '-f',
                               '{}'.format(of.name),
                               '-C',
                               '--export-margin=0',
                               '-d','600',
                               '--export-pdf={}'.format(args.outputfile),
                               '--export-pdf-version=1.5',
    ]))
