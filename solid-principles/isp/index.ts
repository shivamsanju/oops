/*
Instead of creating a single generic interface,
create multiple specific interfaces
*/

interface Printer {
  print(page: string): void;
  fax(page: string): void;
}

class ModernPrinter implements Printer {
  print(page: string): void {
    console.log(page);
  }

  fax(page: string): void {
    // do something
  }
}

class OldPrinter implements Printer {
  print(page: string): void {
    console.log(page);
  }

  fax(page: string): void {
    throw Error("old printer doesn't support fax");
  }
}

/*
The problem above is that we created a generic interface called printer.
which old printers do not support
*/

/****************  SOLUTION *************/

interface Printer2 {
  print(page: string): void;
}

interface FaxMachine {
  fax(page: string): void;
}

class ModernPrinter2 implements Printer2, FaxMachine {
  print(page: string): void {
    console.log(page);
  }

  fax(page: string): void {
    // do something
  }
}

class OldPrinter2 implements Printer2 {
  print(page: string): void {
    console.log(page);
  }
}

/*
Above we created specific interfaces so we can use them more precisely
*/
