#!/usr/bin/python
import sys, getopt, os

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ['help', 'input=', 'outputdir='])
except getopt.GetoptError:
    print "%s -i <inputfile> -o <outputdir>" % (sys.argv[0])
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print "%s -i <inputfile> -o <outputdir>" % (sys.argv[0])
        sys.exit()
    elif opt in ('-i', '--input'):
        ifile = arg
    elif opt in ('-o', '--ouputdir'):
        targetdir = arg

def main(ifile, targetdir):
    file_content = """---
# host_var
# Host: {hostname}
host_name: {hostname}
network_interfaces_hash:
  - interface: {iface}
    ipaddress: {ipaddr}
    netmask: {netmask}
    gateway: {gateway}
    mydomain: 'asx.com.au'
    domain: "asx.com.au asxprod.asx.com.au"
    dns_servers:
    - 203.0.117.15
    - 203.0.118.15
    - 10.2.8.15
"""
    infile=open(ifile, 'r')
    for line in infile:
        hostname, iface, ipaddr, netmask, gateway = line.split()
        print "writing file %s/%s.yaml" %(targetdir, hostname)
        context = {
            'hostname' : hostname,
            'iface' : iface or 'ens192',
            'ipaddr' : ipaddr,
            'netmask' : netmask or '255.255.255.0',
            'gateway' : gateway
        }
        filename = os.path.join(targetdir, hostname + '.yaml')
        ofile = open(filename, 'w')
        ofile.write(file_content.format(**context))
        ofile.close()

    infile.close()

if __name__ == "__main__":

    try:
        fexist=os.path.isfile(ifile)
    except NameError:
        print "provide input file"
        print "%s -i <inputfile> -o <outputdir>" % (sys.argv[0])
        sys.exit(2)
    else:
        if not fexist:
            print "Input file %s does not exist" % (ifile)
            sys.exit(2)

    try:
        texists = os.path.isdir(targetdir)
    except NameError:
        print "provide target directory"
        print "%s -i <inputfile> -o <outputdir>" % (sys.argv[0])
        sys.exit(2)
    else:
        if not texists:
            print "Target directory %s does not exist" % (targetdir)
            sys.exit(2)

    print "Variables input %s and target dir %s:" % (ifile, targetdir)

    main(ifile, targetdir)