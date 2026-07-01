import random

WORD_LIST = [
    "python", "hangman", "developer", "internship", "function",
    "variable", "keyboard", "monitor", "internet", "database",
    "software", "hardware", "network", "algorithm", "debugging",
    "compiler", "interpreter", "framework", "library", "package",
    "exception", "iteration", "recursion", "condition", "boolean",
    "integer", "floating", "string", "character", "syntax",
    "operator", "expression", "statement", "functionality", "parameter",
    "argument", "object", "class", "inheritance", "encapsulation",
    "polymorphism", "abstraction", "method", "attribute", "instance",
    "constructor", "destructor", "module", "package", "directory",
    "filesystem", "process", "thread", "execution", "memory",
    "storage", "binary", "decimal", "hexadecimal", "octal",
    "encryption", "decryption", "security", "authentication", "authorization",
    "frontend", "backend", "fullstack", "application", "deployment",
    "container", "virtualization", "cloud", "server", "client",
    "request", "response", "protocol", "http", "https",
    "api", "endpoint", "json", "xml", "parsing",
    "validation", "testing", "unittest", "integration", "performance",
    "optimization", "scalability", "availability", "reliability", "latency",
    "throughput", "bandwidth", "firewall", "router", "switch",
    "gateway", "session", "cookie", "cache", "buffer"
]

def choose_word():
    return random.choice(WORD_LIST)